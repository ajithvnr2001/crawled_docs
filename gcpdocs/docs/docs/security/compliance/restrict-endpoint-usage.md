---
url: https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage/
title: Restrict endpoint usage \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:27:25.550866+00:00
---

# Restrict endpoint usage  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Restrict endpoint usage Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the **Restrict Endpoint Usage** [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints), which allows enterprise administrators to control which Google Cloud API endpoints can be used within their Google Cloud resource hierarchy.

Administrators can use this constraint to define hierarchical restrictions on allowed Google Cloud API endpoints, such as global, locational, or regional endpoints. For example, you can configure a project to deny requests to the global `bigquery.googleapis.com` endpoint, but allow requests to the locational `LOCATION-bigquery.googleapis.com` endpoint. By restricting global API endpoint usage, organizations can meet compliance requirements by ensuring that only allowed locational or regional endpoints are used.

The Restrict Endpoint Usage constraint is set using a denylist, allowing requests to any supported services' API endpoints that are not explicitly denied.

This constraint controls the runtime access to all in-scope resources. When the organization policy containing this constraint is updated, it immediately applies to all resources within the scope of the policy, with eventual consistency.

**Warning:** An organization policy that includes this constraint will cause service API requests that violate the constraint to fail, which can prevent workloads from working correctly if the constraint is set on existing resources.

We recommend that administrators carefully manage updates to organization policies containing this constraint. For example, you should consider setting the policy in dry-run mode to monitor how a policy change would impact your existing workflows before it is enforced.

## API endpoint types

An API endpoint (or service endpoint) is a URL that specifies the network address of a Google Cloud API service, such as `bigquery.googleapis.com`. Google Cloud services allow access to resources using different types of API endpoints, including global, locational, and regional endpoints. Support for each type depends on the service.

### Global API endpoints

Global API endpoints don't specify the location in the URL hostname. These globally scoped endpoints provide high-availability service endpoints that terminate the TLS session as close to the client as possible, which minimizes latency when serving API calls from a dispersed client population over the internet. However, these endpoints don't provide any regional isolation or data residency compliance.

For applications that can handle global dependencies and need fast performance from Google's global network, you can use global endpoints.

Global endpoints have the following format:

`SERVICE.googleapis.com`

Where `SERVICE` is the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.

### Locational API endpoints

**Note:** Locational API endpoints are supported by a limited number of services, and their availability varies.

Regional API endpoints are replacing locational endpoints. Locational endpoints are regional or multi-regional service hostnames that you can use to access data in a given location.

However, locational endpoints don't support the following features:

  * Data residency compliant connections from on-premises through the internet
  * Failure domain isolation



Locational endpoints specify the location in the URL hostname and have the following format:

`LOCATION-SERVICE.googleapis.com`

  * `LOCATION`: the Google Cloud region name, such as `us-central1`, `europe-west1`, or `us`.
  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.



### Regional API endpoints

Regional API endpoints provide access to Google Cloud services through an API endpoint that is scoped to a single Google Cloud region. Traffic sent to a regional endpoint is processed and TLS terminated entirely within the specified region.

For most Google Cloud services, you can use regional endpoints to work with regional resources within the specified region. Operations on global resources, multi-regional resources, and out-of-region regional resources are typically not supported from the regional endpoint.

Regional API endpoints specify the location as a subdomain. Public regional endpoints have the following format:

`SERVICE.REGION.rep.googleapis.com`

  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.
  * `REGION`: the Google Cloud region name, such as `us-central1` or `europe-west1`.



Private regional API endpoints have the following format:

`SERVICE.REGION.p.rep.googleapis.com`

  * `SERVICE`: the name of the Google Cloud service, such as `storage`, `compute`, or `bigquery`.
  * `REGION`: the Google Cloud region name, such as `us-central1` or `europe-west1`.
  * `.p.`: indicates a private target intended for Private Service Connect connectivity.



## Limitations

The Restrict Endpoint Usage constraint controls the ability to use specific API endpoints to access your resources. It shouldn't be confused with other similar constraints, such as:

  * [Restrict Resource Location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), which controls where resources can or cannot be created.
  * [Restrict Resource Service Usage constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources), which controls which resource services can be used.



To avoid breaking existing serving infrastructure, test any new organization policy on non-production projects and folders, then apply the policy gradually within your organization.

This constraint applies to a specific subset of products and resource types. For a list of supported services and details on the behavior of each service, see the Supported API endpoints section.

For data storage commitments, see the [Google Cloud Terms of Service](https://cloud.google.com/terms) and the [Service Specific Terms](https://cloud.google.com/terms/service-terms). Organization policies that contain the Restrict Endpoint Usage constraint are not data residency commitments.

## Set the organization policy

To set, change, or delete an organization policy, you must have the [Organization Policy Administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin) role.

Organization policy constraints can be set at the organization, folder, and project level. Each policy applies to all resources within its corresponding resource hierarchy, but can be overridden at lower levels in the resource hierarchy.

For more information about policy evaluation, see [Understanding Hierarchy Evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

The Restrict Endpoint Usage constraint is a type of [list constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#list-constraint). You can add and remove endpoints from the `denied_values` lists of the constraint.

### Console

  1. Go to the **Organization policies** page in the Google Cloud console.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the **Project picker** , select the organization, folder, or project for which you want to set the organization policy.

  3. In the table of organization policies, select **Restrict endpoint usage** to open its **Policy details** page.

  4. Click **Manage policy**.

  5. Under **Applies to** , select **Customize**.

  6. Under **Policy enforcement** , choose how to apply inheritance to this policy.

     1. If you want to inherit the organization policy of the parent resource and merge it with this one, select **Merge with parent**.

     2. If you want to override any existing organization policies, select **Replace**.

  7. Click **Add a rule**.

  8. Under **Policy values** , select **Custom**.

  9. Under **Policy type** , select **Deny** to create a list of denied endpoints.

  10. Under **Custom values** , add the API endpoint hostname you want to block to the list.

     1. For example, to block BigQuery's global API endpoint, enter `bigquery.googleapis.com`.

     2. To add more endpoints, click **Add value**.

  11. To enforce the policy, click **Save**.




### gcloud

Organization policies can be set through the [`gcloud resource-manager org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy) command. To enforce an organization policy that includes the **Restrict Endpoint Usage** constraint, first create a YAML file with the policy to be updated:
    
    
    constraint: constraints/gcp.restrictEndpointUsage
    listPolicy:
        deniedValues:
        - storage.googleapis.com
        - content-bigqueryreservation.googleapis.com
        - bigquerystorage.mtls.googleapis.com
        - logging.googleapis.com
    

Replace the following placeholder values with your own before you run the command:

  * RESOURCE_TYPE: The type of resource, either a project or a folder. For example: `project`
  * RESOURCE_ID: The resource ID of the project or folder. For example: `8767234`


    
    
    gcloud resource-manager org-policies set-policy \
    --RESOURCE_TYPE='RESOURCE_ID' /tmp/policy.yaml

The response contains the newly set organization policy:
    
    
    constraint: constraints/gcp.restrictEndpointUsage
    etag: CKCRl6oGEPjG-tMB
    listPolicy:
      deniedValues:
      - storage.googleapis.com
      - content-bigqueryreservation.googleapis.com
      - bigquerystorage.mtls.googleapis.com
      - logging.googleapis.com
    updateTime: '2023-11-04T04:29:20.444507Z'

If a request to a denied API endpoint attempts to access a resource, the request will fail, and an error is returned that describes the reason for this failure.

## Create an organization policy in dry-run mode

An organization policy in dry-run mode is a type of organization policy where violations of the policy are audit logged, but the violating actions aren't denied. You can create an organization policy in dry-run mode using the **Restrict Endpoint Usage** constraint to monitor how it would affect your organization before you enforce the live policy. For more information, see [Create an organization policy in dry-run mode](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy#create_dry_run_list_policy).

## Error message

If you set an organization policy to deny an endpoint, operations using that endpoint within your resource hierarchy fail. An error is returned that describes the reason for this failure. Also, an audit log entry is generated for further monitoring, alerting, or debugging.

### Example error message

In the following example, a curl request using the API endpoint `storage.googleapis.com` fails due to policy enforcement:
    
    
    curl -X GET \
    -H "Authorization: Bearer OAUTH2_TOKEN" \
    -o "SAVE_TO_LOCATION" \
    "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?alt=media"
    
    Access to projects/foo-123 through endpoint storage.googleapis.com was denied by
    the constraints/gcp.restrictEndpointUsage organization policy constraint. To
    access this resource, please use an allowed endpoint.

### Example audit log entry

The following example audit log entry demonstrates when access to a resource is denied:
    
    
    {
      logName: "projects/my-projectid/logs/cloudaudit.googleapis.com%2Fpolicy"
      protoPayload: {
        @type: "type.googleapis.com/google.cloud.audit.AuditLog"
        **s tatus: {
          code: 7
          message: "Access to projects/my-projectid through endpoint bigquery.googleapis.com was denied by the constraints/gcp.restrictEndpointUsage organization policy constraint. To access this resource, please use an allowed endpoint."
        }**
        serviceName: "bigquery.googleapis.com"
        methodName: "google.cloud.bigquery.v2.TableDataService.InsertAll"
        resourceName: "projects/my-projectid"
        authenticationInfo: {
          principalEmail: "user_or_service_account@example.com"
        }
      }
      requestMetadata: {
        callerIp: "123.123.123.123"
      }
      **policyViola tionInfo: {
        orgPolicyViolationInfo: {
          violationInfo: [
            {
              constraint: "constraints/gcp.restrictEndpointUsage"
              checkedValue: "bigquery.googleapis.com"
              constraintViolationInfo: {
                @type: "type.googleapis.com/google.cloud.audit.RestrictEndpointUsageViolationInfo"
                tlsTerminationRegionCode: "US"
              }
              errorMessage: "Restrict endpoint usage Org Policy is violated"
              policyType: LIST_CONSTRAINT
            }
          ]
        }
      }**
      resource: {
        type: "audited_resource"
        labels: {
          project_id: "224034263908"
          method: "google.cloud.bigquery.v2.TableDataService.InsertAll"
          service: "bigquery.googleapis.com"
        }
      }
      severity: "ERROR"
      timestamp: "2024-12-05T01:15:30.332519510Z"
      receiveTimestamp: "2024-08-15T17:55:01.159788588Z"
      insertId: "42"
    }

**Note:** For API requests that use third-party credentials, `authenticationInfo` might not occur in the audit log. If present, the `tlsTerminationRegionCode` field indicates the [CLDR region code](https://cldr.unicode.org/) where TLS termination occurred. This field helps you determine whether data was decrypted outside of your geographic boundaries.

## Supported API endpoints

The Restrict Endpoint Usage constraint supports API endpoints for the products listed in the following table.

For each product, the table provides the primary global API endpoint. However, each product may also support a `SERVICE_NAME.mtls.googleapis.com` variant or a `content-SERVICE_NAME.googleapis.com` variant of their global API endpoint, such as `pubsub.mtls.googleapis.com` or `content-pubsub.googleapis.com`. To restrict all variants of a product's global API endpoint, you can use a value group. Additionally, regional and locational API endpoints for these products are supported by the Restrict Endpoint Usage constraint. Refer to the product's API documentation to determine the full list of global, locational, and regional endpoints available.

Product | API endpoints | Notes  
---|---|---  
API Gateway  |  Global API endpoints: 

  * `apigateway.googleapis.com`

  
|  None   
API keys  |  Global API endpoints: 

  * `apikeys.googleapis.com`

  
|  None   
Access Approval  |  Global API endpoints: 

  * `accessapproval.googleapis.com`

  
|  None   
Access Context Manager  |  Global API endpoints: 

  * `accesscontextmanager.googleapis.com`

  
|  None   
Agent Identity API  |  Global API endpoints: 

  * `agentidentity.googleapis.com`

  
|  None   
Agent Identity Credentials API  |  Global API endpoints: 

  * `agentidentitycredentials.googleapis.com`

  
|  None   
Agent Registry  |  Global API endpoints: 

  * `agentregistry.googleapis.com`
  * `apphubendpoint.googleapis.com`

  
|  None   
Apigee API hub  |  Global API endpoints: 

  * `apihub.googleapis.com`

  
|  None   
Apigee API Management API  |  Global API endpoints: 

  * `apim.googleapis.com`

  
|  None   
Apigee Connect API  |  Global API endpoints: 

  * `apigeeconnect.googleapis.com`

  
|  None   
Apigee portal API  |  Global API endpoints: 

  * `apigeeportal.googleapis.com`

  
|  None   
Apigee Registry API  |  Global API endpoints: 

  * `apigeeregistry.googleapis.com`

  
|  None   
Apigee  |  Global API endpoints: 

  * `apigee.googleapis.com`

  
|  None   
App Config Manager API  |  Global API endpoints: 

  * `appconfigmanager.googleapis.com`

  
|  None   
Application Design Center  |  Global API endpoints: 

  * `designcenter.googleapis.com`

  
|  None   
Application Integration  |  Global API endpoints: 

  * `integrations.googleapis.com`

  
|  None   
Artifact Analysis  |  Global API endpoints: 

  * `containeranalysis.googleapis.com`
  * `ondemandscanning.googleapis.com`

  
|  None   
Artifact Registry  |  Global API endpoints: 

  * `artifactregistry.googleapis.com`

  
|  None   
Assured Open Source Software  |  Global API endpoints: 

  * `assuredoss.googleapis.com`

  
|  None   
Assured Workloads  |  Global API endpoints: 

  * `assuredworkloads.googleapis.com`

  
|  None   
Audit Manager  |  Global API endpoints: 

  * `auditmanager.googleapis.com`

  
|  None   
Authorization Toolkit API  |  Global API endpoints: 

  * `authztoolkit.googleapis.com`

  
|  None   
Backup and DR Service  |  Global API endpoints: 

  * `backupdr.googleapis.com`

  
|  None   
Backup for GKE  |  Global API endpoints: 

  * `gkebackup.googleapis.com`

  
|  None   
Batch  |  Global API endpoints: 

  * `batch.googleapis.com`

  
|  None   
Chrome Enterprise Premium  |  Global API endpoints: 

  * `beyondcorp.googleapis.com`

  
|  None   
Lakehouse  |  Global API endpoints: 

  * `biglake.googleapis.com`

  
Regional API endpoints: 

  * `biglake.asia-south1.rep.googleapis.com`
  * `biglake.asia-south2.rep.googleapis.com`
  * `biglake.europe-west1.rep.googleapis.com`
  * `biglake.europe-west10.rep.googleapis.com`
  * `biglake.europe-west2.rep.googleapis.com`
  * `biglake.europe-west3.rep.googleapis.com`
  * `biglake.europe-west4.rep.googleapis.com`
  * `biglake.europe-west6.rep.googleapis.com`
  * `biglake.europe-west8.rep.googleapis.com`
  * `biglake.europe-west9.rep.googleapis.com`
  * `biglake.me-central2.rep.googleapis.com`
  * `biglake.northamerica-northeast1.rep.googleapis.com`
  * `biglake.northamerica-northeast2.rep.googleapis.com`
  * `biglake.us-central1.rep.googleapis.com`
  * `biglake.us-east1.rep.googleapis.com`
  * `biglake.us-east4.rep.googleapis.com`
  * `biglake.us-east5.rep.googleapis.com`
  * `biglake.us-south1.rep.googleapis.com`
  * `biglake.us-west1.rep.googleapis.com`
  * `biglake.us-west2.rep.googleapis.com`
  * `biglake.us-west3.rep.googleapis.com`
  * `biglake.us-west4.rep.googleapis.com`

  
|  None   
BigQuery Connections  |  Global API endpoints: 

  * `bigqueryconnection.googleapis.com`

  
|  None   
BigQuery Data Policy  |  Global API endpoints: 

  * `bigquerydatapolicy.googleapis.com`

  
|  None   
BigQuery Data Transfer  |  Global API endpoints: 

  * `bigquerydatatransfer.googleapis.com`

  
|  None   
BigQuery Migration  |  Global API endpoints: 

  * `bigquerymigration.googleapis.com`

  
|  None   
BigQuery Reservation  |  Global API endpoints: 

  * `bigqueryreservation.googleapis.com`

  
|  None   
BigQuery Saved Query API  |  Global API endpoints: 

  * `bigquery-sq.googleapis.com`

  
|  None   
BigQuery Storage  |  Global API endpoints: 

  * `bigquerystorage.googleapis.com`

  
|  None   
BigQuery  |  Global API endpoints: 

  * `bigquery.googleapis.com`
  * `www.googleapis.com (BigQuery)`

  
|  `www.googleapis.com/.../bigquery/...` is a legacy API endpoint format. Your organization should use the newer APIs instead. You can add `www.googleapis.com (BigQuery)` to the Restrict Endpoint Usage policy constraint to avoid accidental use of the old APIs.   
Binary Authorization  |  Global API endpoints: 

  * `binaryauthorization.googleapis.com`

  
|  None   
Blockchain Analytics  |  Global API endpoints: 

  * `blockchain.googleapis.com`

  
|  None   
Blockchain Node Engine  |  Global API endpoints: 

  * `blockchainnodeengine.googleapis.com`

  
|  None   
Blockchain Validator Manager  |  Global API endpoints: 

  * `blockchainvalidatormanager.googleapis.com`

  
|  None   
Business AI Code API  |  Global API endpoints: 

  * `businessaicode.googleapis.com`

  
Regional API endpoints: 

  * `businessaicode.eu.rep.googleapis.com`
  * `businessaicode.us.rep.googleapis.com`

  
|  Supports Google Antigravity in Gemini Enterprise and Gemini Code Assist.   
Capacity Planner  |  Global API endpoints: 

  * `capacityplanner.googleapis.com`

  
|  None   
Certificate Authority Service  |  Global API endpoints: 

  * `privateca.googleapis.com`

  
|  None   
Certificate Manager  |  Global API endpoints: 

  * `certificatemanager.googleapis.com`

  
|  None   
Cloud Asset Inventory  |  Global API endpoints: 

  * `cloudasset.googleapis.com`

  
|  None   
Bigtable  |  Global API endpoints: 

  * `bigtable.googleapis.com`
  * `bigtableadmin.googleapis.com`

  
|  None   
Cloud Billing  |  Global API endpoints: 

  * `cloudbilling.googleapis.com`

  
|  None   
Cloud Build  |  Global API endpoints: 

  * `cloudbuild.googleapis.com`

  
|  None   
Cloud CDN  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Cloud Commerce Producer API  |  Global API endpoints: 

  * `cloudcommerceproducer.googleapis.com`

  
|  None   
Managed Service for Apache Airflow  |  Global API endpoints: 

  * `composer.googleapis.com`

  
|  None   
Cloud Controls Partner API  |  Global API endpoints: 

  * `cloudcontrolspartner.googleapis.com`

  
|  None   
Cloud DNS  |  Global API endpoints: 

  * `dns.googleapis.com`

  
|  None   
Cloud Data Fusion  |  Global API endpoints: 

  * `datafusion.googleapis.com`

  
|  None   
Cloud Deploy  |  Global API endpoints: 

  * `clouddeploy.googleapis.com`

  
|  None   
Cloud Deployment Manager  |  Global API endpoints: 

  * `runtimeconfig.googleapis.com`
  * `deploymentmanager.googleapis.com`

  
|  None   
Cloud Domains  |  Global API endpoints: 

  * `domains.googleapis.com`

  
|  None   
Cloud Healthcare API  |  Global API endpoints: 

  * `healthcare.googleapis.com`

  
|  None   
Cloud Interconnect  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Cloud Intrusion Detection System  |  Global API endpoints: 

  * `ids.googleapis.com`

  
|  None   
Cloud Key Management Service  |  Global API endpoints: 

  * `cloudkms.googleapis.com`

  
|  None   
Cloud Life Sciences  |  Global API endpoints: 

  * `lifesciences.googleapis.com`

  
|  None   
Cloud Load Balancing  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Cloud Logging  |  Global API endpoints: 

  * `logging.googleapis.com`

  
|  None   
Cloud Monitoring  |  Global API endpoints: 

  * `monitoring.googleapis.com`

  
|  None   
Cloud NAT  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Cloud Natural Language API  |  Global API endpoints: 

  * `language.googleapis.com`

  
|  None   
Cloud Next Generation Firewall Enterprise  |  Global API endpoints: 

  * `networksecurity.googleapis.com`

  
|  None   
Cloud Next Generation Firewall Essentials  |  Global API endpoints: 

  * `compute.googleapis.com`
  * `networksecurity.googleapis.com`

  
|  None   
Cloud Next Generation Firewall Standard  |  Global API endpoints: 

  * `compute.googleapis.com`
  * `networksecurity.googleapis.com`

  
|  None   
Cloud OS Login API  |  Global API endpoints: 

  * `oslogin.googleapis.com`

  
|  None   
Cloud Quotas  |  Global API endpoints: 

  * `cloudquotas.googleapis.com`

  
|  None   
Cloud Router  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Cloud Run  |  Global API endpoints: 

  * `run.googleapis.com`

  
|  None   
Cloud SQL  |  Global API endpoints: 

  * `sqladmin.googleapis.com`

  
|  None   
Cloud Scheduler  |  Global API endpoints: 

  * `cloudscheduler.googleapis.com`

  
|  None   
Cloud Service Mesh  |  Global API endpoints: 

  * `meshconfig.googleapis.com`
  * `networksecurity.googleapis.com`
  * `networkservices.googleapis.com`
  * `trafficdirector.googleapis.com`

  
|  None   
Spanner  |  Global API endpoints: 

  * `spanner.googleapis.com`

  
|  None   
Cloud Storage  |  Global API endpoints: 

  * `storage.googleapis.com`
  * `storage-download.googleapis.com`
  * `storage-upload.googleapis.com`
  * `www.googleapis.com (Cloud Storage)`

  
|  The endpoints `storage-download.googleapis.com`, `storage-upload.googleapis.com`, and `www.googleapis.com/.../storage/...` are legacy API endpoint formats. Your organization should use the newer `storage.googleapis.com` API endpoint instead. To prevent accidental use of the legacy APIs, you can add `storage-download.googleapis.com`, `storage-upload.googleapis.com`, and `www.googleapis.com (Cloud Storage)` to the Restrict Endpoint Usage policy constraint denylist.  
  
Some Cloud Storage operations are not supported when using locational endpoints. See [Locational endpoints](https://docs.cloud.google.com/storage/docs/locational-endpoints#supported-operations) for more information. If you configured the Restrict Endpoint Usage constraint to restrict global endpoints, you can use the Google Cloud console to perform these operations. These operations don't carry Customer Data as defined in the data residency service terms, and you can use them in the Google Cloud console without violating ITAR compliance.  
  
[Virtual hosted-style endpoints](https://docs.cloud.google.com/storage/docs/request-endpoints#xml-api) for the global endpoint are not supported at this time (e.g. `https://BUCKET_NAME.storage.googleapis.com`).  
  
  
Cloud Support API  |  Global API endpoints: 

  * `cloudsupport.googleapis.com`

  
|  None   
Cloud Tasks  |  Global API endpoints: 

  * `cloudtasks.googleapis.com`

  
|  None   
Cloud Tool Results API  |  Global API endpoints: 

  * `toolresults.googleapis.com`

  
|  None   
Cloud TPU API  |  Global API endpoints: 

  * `tpu.googleapis.com`

  
|  None   
Cloud Trace API  |  Global API endpoints: 

  * `cloudtrace.googleapis.com`

  
|  None   
Cloud VPN  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Cloud Workstations  |  Global API endpoints: 

  * `workstations.googleapis.com`

  
|  None   
Cluster Director  |  Global API endpoints: 

  * `hypercomputecluster.googleapis.com`

  
|  None   
Commerce Agreement Publishing API  |  Global API endpoints: 

  * `commerceagreementpublishing.googleapis.com`

  
|  None   
Commerce Business Enablement API  |  Global API endpoints: 

  * `commercebusinessenablement.googleapis.com`

  
|  None   
Commerce Price Management API  |  Global API endpoints: 

  * `commercepricemanagement.googleapis.com`

  
|  None   
Compliance Manager  |  Global API endpoints: 

  * `cloudsecuritycompliance.googleapis.com`

  
|  None   
Compute Engine  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Confidential Computing  |  Global API endpoints: 

  * `confidentialcomputing.googleapis.com`

  
|  None   
Connect  |  Global API endpoints: 

  * `gkeconnect.googleapis.com`

  
|  None   
Connect gateway  |  Global API endpoints: 

  * `connectgateway.googleapis.com`

  
|  None   
Contact Center AI Platform API  |  Global API endpoints: 

  * `contactcenteraiplatform.googleapis.com`

  
|  None   
Container Threat Detection  |  Global API endpoints: 

  * `containerthreatdetection.googleapis.com`

  
|  None   
Content Warehouse API  |  Global API endpoints: 

  * `contentwarehouse.googleapis.com`

  
|  None   
Context-Aware Access  |  Global API endpoints: 

  * `accesscontextmanager.googleapis.com`

  
|  None   
Continuous Validation API  |  Global API endpoints: 

  * `continuousvalidation.googleapis.com`

  
|  None   
Dialogflow CX  |  Global API endpoints: 

  * `dialogflow.googleapis.com`

  
  
Locational API endpoints: 

  * `asia-northeast1-dialogflow.googleapis.com`
  * `asia-northeast3-dialogflow.googleapis.com`
  * `asia-south1-dialogflow.googleapis.com`
  * `asia-southeast1-dialogflow.googleapis.com`
  * `asia-southeast2-dialogflow.googleapis.com`
  * `australia-southeast1-dialogflow.googleapis.com`
  * `eu-dialogflow.googleapis.com`
  * `europe-west1-dialogflow.googleapis.com`
  * `europe-west2-dialogflow.googleapis.com`
  * `europe-west3-dialogflow.googleapis.com`
  * `europe-west4-dialogflow.googleapis.com`
  * `europe-west6-dialogflow.googleapis.com`
  * `europe-west8-dialogflow.googleapis.com`
  * `me-central2-dialogflow.googleapis.com`
  * `me-west1-dialogflow.googleapis.com`
  * `northamerica-northeast1-dialogflow.googleapis.com`
  * `northamerica-northeast2-dialogflow.googleapis.com`
  * `us-central1-dialogflow.googleapis.com`
  * `us-dialogflow.googleapis.com`
  * `us-east1-dialogflow.googleapis.com`
  * `us-west1-dialogflow.googleapis.com`

  
|  None   
Data Labeling API  |  Global API endpoints: 

  * `datalabeling.googleapis.com`

  
|  None   
Data Security Posture Management API  |  Global API endpoints: 

  * `dspm.googleapis.com`

  
|  None   
Database Center  |  Global API endpoints: 

  * `databasecenter.googleapis.com`

  
|  None   
Database Migration Service  |  Global API endpoints: 

  * `datamigration.googleapis.com`

  
|  None   
Dataform  |  Global API endpoints: 

  * `dataform.googleapis.com`

  
|  None   
Dataflow  |  Global API endpoints: 

  * `dataflow.googleapis.com`

  
|  None   
Knowledge Catalog  |  Global API endpoints: 

  * `dataplex.googleapis.com`
  * `datalineage.googleapis.com`

  
|  None   
Managed Service for Apache Spark  |  Global API endpoints: 

  * `dataproc.googleapis.com`

  
|  None   
Dataproc on GDC  |  Global API endpoints: 

  * `dataprocgdc.googleapis.com`

  
|  None   
Datastream  |  Global API endpoints: 

  * `datastream.googleapis.com`

  
|  None   
Developer Connect  |  Global API endpoints: 

  * `developerconnect.googleapis.com`

  
|  None   
Google Distributed Cloud  |  Global API endpoints: 

  * `opsconfigmonitoring.googleapis.com`
  * `gdcvmmanager.googleapis.com`
  * `gdchardwaremanagement.googleapis.com`

  
|  None   
Distributed Cloud Edge Container API  |  Global API endpoints: 

  * `edgecontainer.googleapis.com`

  
|  None   
Distributed Cloud Edge Network API  |  Global API endpoints: 

  * `edgenetwork.googleapis.com`

  
|  None   
Document AI  |  Global API endpoints: 

  * `documentai.googleapis.com`

  
  
Locational API endpoints: 

  * `asia-south1-documentai.googleapis.com`
  * `asia-southeast1-documentai.googleapis.com`
  * `australia-southeast1-documentai.googleapis.com`
  * `eu-documentai.googleapis.com`
  * `europe-west2-documentai.googleapis.com`
  * `europe-west3-documentai.googleapis.com`
  * `northamerica-northeast1-documentai.googleapis.com`
  * `us-documentai.googleapis.com`

  
|  None   
Enterprise Knowledge Graph  |  Global API endpoints: 

  * `enterpriseknowledgegraph.googleapis.com`

  
|  None   
Error Reporting  |  Global API endpoints: 

  * `clouderrorreporting.googleapis.com`

  
|  None   
Essential Contacts  |  Global API endpoints: 

  * `essentialcontacts.googleapis.com`

  
|  None   
Eventarc API  |  Global API endpoints: 

  * `eventarc.googleapis.com`

  
|  None   
Filestore  |  Global API endpoints: 

  * `file.googleapis.com`

  
|  None   
Firestore  |  Global API endpoints: 

  * `firestore.googleapis.com`

  
  
Locational API endpoints: 

  * `africa-south1-firestore.googleapis.com`
  * `asia-east1-firestore.googleapis.com`
  * `asia-east2-firestore.googleapis.com`
  * `asia-northeast1-firestore.googleapis.com`
  * `asia-northeast2-firestore.googleapis.com`
  * `asia-northeast3-firestore.googleapis.com`
  * `asia-south1-firestore.googleapis.com`
  * `asia-south2-firestore.googleapis.com`
  * `asia-southeast1-firestore.googleapis.com`
  * `asia-southeast2-firestore.googleapis.com`
  * `australia-southeast1-firestore.googleapis.com`
  * `australia-southeast2-firestore.googleapis.com`
  * `eur3-firestore.googleapis.com`
  * `europe-central2-firestore.googleapis.com`
  * `europe-north1-firestore.googleapis.com`
  * `europe-north2-firestore.googleapis.com`
  * `europe-southwest1-firestore.googleapis.com`
  * `europe-west1-firestore.googleapis.com`
  * `europe-west2-firestore.googleapis.com`
  * `europe-west3-firestore.googleapis.com`
  * `europe-west4-firestore.googleapis.com`
  * `europe-west6-firestore.googleapis.com`
  * `europe-west8-firestore.googleapis.com`
  * `europe-west9-firestore.googleapis.com`
  * `europe-west10-firestore.googleapis.com`
  * `europe-west12-firestore.googleapis.com`
  * `me-central1-firestore.googleapis.com`
  * `me-central2-firestore.googleapis.com`
  * `me-west1-firestore.googleapis.com`
  * `nam5-firestore.googleapis.com`
  * `nam7-firestore.googleapis.com`
  * `northamerica-northeast1-firestore.googleapis.com`
  * `northamerica-northeast2-firestore.googleapis.com`
  * `northamerica-south1-firestore.googleapis.com`
  * `southamerica-east1-firestore.googleapis.com`
  * `southamerica-west1-firestore.googleapis.com`
  * `us-central1-firestore.googleapis.com`
  * `us-east1-firestore.googleapis.com`
  * `us-east4-firestore.googleapis.com`
  * `us-east5-firestore.googleapis.com`
  * `us-south1-firestore.googleapis.com`
  * `us-west1-firestore.googleapis.com`
  * `us-west2-firestore.googleapis.com`
  * `us-west3-firestore.googleapis.com`
  * `us-west4-firestore.googleapis.com`

  
Regional API endpoints: 

  * `firestore.africa-south1.rep.googleapis.com`
  * `firestore.asia-east1.rep.googleapis.com`
  * `firestore.asia-east2.rep.googleapis.com`
  * `firestore.asia-northeast1.rep.googleapis.com`
  * `firestore.asia-northeast2.rep.googleapis.com`
  * `firestore.asia-northeast3.rep.googleapis.com`
  * `firestore.asia-south1.rep.googleapis.com`
  * `firestore.asia-south2.rep.googleapis.com`
  * `firestore.asia-southeast1.rep.googleapis.com`
  * `firestore.asia-southeast2.rep.googleapis.com`
  * `firestore.australia-southeast1.rep.googleapis.com`
  * `firestore.australia-southeast2.rep.googleapis.com`
  * `firestore.eu.rep.googleapis.com`
  * `firestore.europe-central2.rep.googleapis.com`
  * `firestore.europe-north1.rep.googleapis.com`
  * `firestore.europe-north2.rep.googleapis.com`
  * `firestore.europe-southwest1.rep.googleapis.com`
  * `firestore.europe-west1.rep.googleapis.com`
  * `firestore.europe-west10.rep.googleapis.com`
  * `firestore.europe-west12.rep.googleapis.com`
  * `firestore.europe-west2.rep.googleapis.com`
  * `firestore.europe-west3.rep.googleapis.com`
  * `firestore.europe-west4.rep.googleapis.com`
  * `firestore.europe-west6.rep.googleapis.com`
  * `firestore.europe-west8.rep.googleapis.com`
  * `firestore.europe-west9.rep.googleapis.com`
  * `firestore.me-central1.rep.googleapis.com`
  * `firestore.me-central2.rep.googleapis.com`
  * `firestore.me-west1.rep.googleapis.com`
  * `firestore.northamerica-northeast1.rep.googleapis.com`
  * `firestore.northamerica-northeast2.rep.googleapis.com`
  * `firestore.northamerica-south1.rep.googleapis.com`
  * `firestore.southamerica-east1.rep.googleapis.com`
  * `firestore.southamerica-west1.rep.googleapis.com`
  * `firestore.us.rep.googleapis.com`
  * `firestore.us-central1.rep.googleapis.com`
  * `firestore.us-east1.rep.googleapis.com`
  * `firestore.us-east4.rep.googleapis.com`
  * `firestore.us-east5.rep.googleapis.com`
  * `firestore.us-south1.rep.googleapis.com`
  * `firestore.us-west1.rep.googleapis.com`
  * `firestore.us-west2.rep.googleapis.com`
  * `firestore.us-west3.rep.googleapis.com`
  * `firestore.us-west4.rep.googleapis.com`

  
|  None   
Firestore in Datastore mode (Datastore)  |  Global API endpoints: 

  * `datastore.googleapis.com`

  
  
Locational API endpoints: 

  * `africa-south1-datastore.googleapis.com`
  * `asia-east1-datastore.googleapis.com`
  * `asia-east2-datastore.googleapis.com`
  * `asia-northeast1-datastore.googleapis.com`
  * `asia-northeast2-datastore.googleapis.com`
  * `asia-northeast3-datastore.googleapis.com`
  * `asia-south1-datastore.googleapis.com`
  * `asia-south2-datastore.googleapis.com`
  * `asia-southeast1-datastore.googleapis.com`
  * `asia-southeast2-datastore.googleapis.com`
  * `australia-southeast1-datastore.googleapis.com`
  * `australia-southeast2-datastore.googleapis.com`
  * `eur3-datastore.googleapis.com`
  * `europe-central2-datastore.googleapis.com`
  * `europe-north1-datastore.googleapis.com`
  * `europe-north2-datastore.googleapis.com`
  * `europe-southwest1-datastore.googleapis.com`
  * `europe-west1-datastore.googleapis.com`
  * `europe-west2-datastore.googleapis.com`
  * `europe-west3-datastore.googleapis.com`
  * `europe-west4-datastore.googleapis.com`
  * `europe-west6-datastore.googleapis.com`
  * `europe-west8-datastore.googleapis.com`
  * `europe-west9-datastore.googleapis.com`
  * `europe-west10-datastore.googleapis.com`
  * `europe-west12-datastore.googleapis.com`
  * `me-central1-datastore.googleapis.com`
  * `me-central2-datastore.googleapis.com`
  * `me-west1-datastore.googleapis.com`
  * `nam5-datastore.googleapis.com`
  * `nam7-datastore.googleapis.com`
  * `northamerica-northeast1-datastore.googleapis.com`
  * `northamerica-northeast2-datastore.googleapis.com`
  * `northamerica-south1-datastore.googleapis.com`
  * `southamerica-east1-datastore.googleapis.com`
  * `southamerica-west1-datastore.googleapis.com`
  * `us-central1-datastore.googleapis.com`
  * `us-east1-datastore.googleapis.com`
  * `us-east4-datastore.googleapis.com`
  * `us-east5-datastore.googleapis.com`
  * `us-south1-datastore.googleapis.com`
  * `us-west1-datastore.googleapis.com`
  * `us-west2-datastore.googleapis.com`
  * `us-west3-datastore.googleapis.com`
  * `us-west4-datastore.googleapis.com`

  
Regional API endpoints: 

  * `datastore.africa-south1.rep.googleapis.com`
  * `datastore.asia-east1.rep.googleapis.com`
  * `datastore.asia-east2.rep.googleapis.com`
  * `datastore.asia-northeast1.rep.googleapis.com`
  * `datastore.asia-northeast2.rep.googleapis.com`
  * `datastore.asia-northeast3.rep.googleapis.com`
  * `datastore.asia-south1.rep.googleapis.com`
  * `datastore.asia-south2.rep.googleapis.com`
  * `datastore.asia-southeast1.rep.googleapis.com`
  * `datastore.asia-southeast2.rep.googleapis.com`
  * `datastore.australia-southeast1.rep.googleapis.com`
  * `datastore.australia-southeast2.rep.googleapis.com`
  * `datastore.eu.rep.googleapis.com`
  * `datastore.europe-central2.rep.googleapis.com`
  * `datastore.europe-north1.rep.googleapis.com`
  * `datastore.europe-north2.rep.googleapis.com`
  * `datastore.europe-southwest1.rep.googleapis.com`
  * `datastore.europe-west1.rep.googleapis.com`
  * `datastore.europe-west10.rep.googleapis.com`
  * `datastore.europe-west12.rep.googleapis.com`
  * `datastore.europe-west2.rep.googleapis.com`
  * `datastore.europe-west3.rep.googleapis.com`
  * `datastore.europe-west4.rep.googleapis.com`
  * `datastore.europe-west6.rep.googleapis.com`
  * `datastore.europe-west8.rep.googleapis.com`
  * `datastore.europe-west9.rep.googleapis.com`
  * `datastore.me-central1.rep.googleapis.com`
  * `datastore.me-central2.rep.googleapis.com`
  * `datastore.me-west1.rep.googleapis.com`
  * `datastore.northamerica-northeast1.rep.googleapis.com`
  * `datastore.northamerica-northeast2.rep.googleapis.com`
  * `datastore.northamerica-south1.rep.googleapis.com`
  * `datastore.southamerica-east1.rep.googleapis.com`
  * `datastore.southamerica-west1.rep.googleapis.com`
  * `datastore.us.rep.googleapis.com`
  * `datastore.us-central1.rep.googleapis.com`
  * `datastore.us-east1.rep.googleapis.com`
  * `datastore.us-east4.rep.googleapis.com`
  * `datastore.us-east5.rep.googleapis.com`
  * `datastore.us-south1.rep.googleapis.com`
  * `datastore.us-west1.rep.googleapis.com`
  * `datastore.us-west2.rep.googleapis.com`
  * `datastore.us-west3.rep.googleapis.com`
  * `datastore.us-west4.rep.googleapis.com`

  
|  None   
Financial Services API  |  Global API endpoints: 

  * `financialservices.googleapis.com`

  
|  None   
Firebase AI Logic  |  Global API endpoints: 

  * `firebasevertexai.googleapis.com`

  
|  None   
Firebase App Hosting  |  Global API endpoints: 

  * `firebaseapphosting.googleapis.com`

  
|  None   
Firebase Data Connect  |  Global API endpoints: 

  * `firebasedataconnect.googleapis.com`

  
|  None   
Firebase Security Rules  |  Global API endpoints: 

  * `firebaserules.googleapis.com`

  
|  None   
Generative AI on Gemini Enterprise Agent Platform  |  Global API endpoints: 

  * `aiplatform.googleapis.com`

  
  
Locational API endpoints: 

  * `africa-south1-aiplatform.googleapis.com`
  * `asia-east1-aiplatform.googleapis.com`
  * `asia-east2-aiplatform.googleapis.com`
  * `asia-northeast1-aiplatform.googleapis.com`
  * `asia-northeast2-aiplatform.googleapis.com`
  * `asia-northeast3-aiplatform.googleapis.com`
  * `asia-south1-aiplatform.googleapis.com`
  * `asia-south2-aiplatform.googleapis.com`
  * `asia-southeast1-aiplatform.googleapis.com`
  * `asia-southeast2-aiplatform.googleapis.com`
  * `australia-southeast1-aiplatform.googleapis.com`
  * `australia-southeast2-aiplatform.googleapis.com`
  * `eu-aiplatform.googleapis.com`
  * `europe-central2-aiplatform.googleapis.com`
  * `europe-north1-aiplatform.googleapis.com`
  * `europe-north2-aiplatform.googleapis.com`
  * `europe-southwest1-aiplatform.googleapis.com`
  * `europe-west1-aiplatform.googleapis.com`
  * `europe-west2-aiplatform.googleapis.com`
  * `europe-west3-aiplatform.googleapis.com`
  * `europe-west4-aiplatform.googleapis.com`
  * `europe-west6-aiplatform.googleapis.com`
  * `europe-west8-aiplatform.googleapis.com`
  * `europe-west9-aiplatform.googleapis.com`
  * `europe-west10-aiplatform.googleapis.com`
  * `europe-west12-aiplatform.googleapis.com`
  * `me-central1-aiplatform.googleapis.com`
  * `me-central2-aiplatform.googleapis.com`
  * `me-west1-aiplatform.googleapis.com`
  * `northamerica-northeast1-aiplatform.googleapis.com`
  * `northamerica-northeast2-aiplatform.googleapis.com`
  * `southamerica-east1-aiplatform.googleapis.com`
  * `southamerica-west1-aiplatform.googleapis.com`
  * `us-aiplatform.googleapis.com`
  * `us-central1-aiplatform.googleapis.com`
  * `us-east1-aiplatform.googleapis.com`
  * `us-east4-aiplatform.googleapis.com`
  * `us-east5-aiplatform.googleapis.com`
  * `us-south1-aiplatform.googleapis.com`
  * `us-west1-aiplatform.googleapis.com`
  * `us-west2-aiplatform.googleapis.com`
  * `us-west3-aiplatform.googleapis.com`
  * `us-west4-aiplatform.googleapis.com`
  * `us-west8-aiplatform.googleapis.com`

  
Regional API endpoints: 

  * `aiplatform.africa-south1.rep.googleapis.com`
  * `aiplatform.asia-east1.rep.googleapis.com`
  * `aiplatform.asia-east2.rep.googleapis.com`
  * `aiplatform.asia-northeast1.rep.googleapis.com`
  * `aiplatform.asia-northeast2.rep.googleapis.com`
  * `aiplatform.asia-northeast3.rep.googleapis.com`
  * `aiplatform.asia-south1.rep.googleapis.com`
  * `aiplatform.asia-south2.rep.googleapis.com`
  * `aiplatform.asia-southeast1.rep.googleapis.com`
  * `aiplatform.asia-southeast2.rep.googleapis.com`
  * `aiplatform.australia-southeast1.rep.googleapis.com`
  * `aiplatform.australia-southeast2.rep.googleapis.com`
  * `aiplatform.eu.rep.googleapis.com`
  * `aiplatform.europe-central2.rep.googleapis.com`
  * `aiplatform.europe-north1.rep.googleapis.com`
  * `aiplatform.europe-north2.rep.googleapis.com`
  * `aiplatform.europe-southwest1.rep.googleapis.com`
  * `aiplatform.europe-west1.rep.googleapis.com`
  * `aiplatform.europe-west2.rep.googleapis.com`
  * `aiplatform.europe-west3.rep.googleapis.com`
  * `aiplatform.europe-west4.rep.googleapis.com`
  * `aiplatform.europe-west6.rep.googleapis.com`
  * `aiplatform.europe-west8.rep.googleapis.com`
  * `aiplatform.europe-west9.rep.googleapis.com`
  * `aiplatform.europe-west10.rep.googleapis.com`
  * `aiplatform.europe-west12.rep.googleapis.com`
  * `aiplatform.me-central1.rep.googleapis.com`
  * `aiplatform.me-central2.rep.googleapis.com`
  * `aiplatform.me-west1.rep.googleapis.com`
  * `aiplatform.northamerica-northeast1.rep.googleapis.com`
  * `aiplatform.northamerica-northeast2.rep.googleapis.com`
  * `aiplatform.southamerica-east1.rep.googleapis.com`
  * `aiplatform.southamerica-west1.rep.googleapis.com`
  * `aiplatform.us-central1.rep.googleapis.com`
  * `aiplatform.us-east1.rep.googleapis.com`
  * `aiplatform.us-east4.rep.googleapis.com`
  * `aiplatform.us-east5.rep.googleapis.com`
  * `aiplatform.us-south1.rep.googleapis.com`
  * `aiplatform.us-west1.rep.googleapis.com`
  * `aiplatform.us-west2.rep.googleapis.com`
  * `aiplatform.us-west3.rep.googleapis.com`
  * `aiplatform.us-west4.rep.googleapis.com`
  * `aiplatform.us-west8.rep.googleapis.com`
  * `aiplatform.us.rep.googleapis.com`

  
|  Shares underlying API endpoints with Gemini Enterprise Agent Platform and Vector Search. Endpoint restrictions applied to these endpoints affect all Vertex AI services. You can also manage access using the curated `in:*-aiplatform-endpoints` value groups (such as `in:global-aiplatform-endpoints`, `in:aiplatform-us-endpoints`, and `in:non-us-aiplatform-endpoints`).   
GKE Dataplane Management  |  Global API endpoints: 

  * `gkedataplanemanagement.googleapis.com`

  
|  None   
GKE Enterprise Edge API  |  Global API endpoints: 

  * `anthosedge.googleapis.com`

  
|  None   
GKE Fleet (Fleet)  |  Global API endpoints: 

  * `gkehub.googleapis.com`

  
|  None   
GKE Multi-Cloud  |  Global API endpoints: 

  * `gkemulticloud.googleapis.com`

  
|  None   
GKE On-Prem API  |  Global API endpoints: 

  * `gkeonprem.googleapis.com`

  
|  None   
Gemini Enterprise  |  Global API endpoints: 

  * `discoveryengine.googleapis.com`

  
  
Locational API endpoints: 

  * `eu-discoveryengine.googleapis.com`
  * `us-discoveryengine.googleapis.com`

  
|  None   
Gemini for Google Cloud API  |  Global API endpoints: 

  * `cloudaicompanion.googleapis.com`

  
|  None   
Google Antigravity for Enterprise  |  Global API endpoints: 

  * `businessaicode.googleapis.com`

  
Regional API endpoints: 

  * `businessaicode.eu.rep.googleapis.com`
  * `businessaicode.us.rep.googleapis.com`

  
|  None   
Google Cloud API  |  Global API endpoints: 

  * `cloud.googleapis.com`

  
|  None   
Google Cloud Armor  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Google Cloud Migration Center  |  Global API endpoints: 

  * `migrationcenter.googleapis.com`

  
|  None   
Google Cloud NetApp Volumes  |  Global API endpoints: 

  * `netapp.googleapis.com`

  
|  None   
Google Cloud Observability  |  Global API endpoints: 

  * `stackdriver.googleapis.com`

  
|  None   
Google Kubernetes Engine  |  Global API endpoints: 

  * `container.googleapis.com`
  * `configdelivery.googleapis.com`

  
|  None   
Google Security Operations Partner API  |  Global API endpoints: 

  * `chroniclepartner.googleapis.com`

  
|  None   
Google Security Operations  |  Restricting global API endpoints isn't supported.  
  
Locational API endpoints: 

  * `africa-south1-chronicle.googleapis.com`
  * `asia-northeast1-chronicle.googleapis.com`
  * `asia-south1-chronicle.googleapis.com`
  * `asia-southeast1-chronicle.googleapis.com`
  * `asia-southeast2-chronicle.googleapis.com`
  * `australia-southeast1-chronicle.googleapis.com`
  * `eu-chronicle.googleapis.com`
  * `europe-west2-chronicle.googleapis.com`
  * `europe-west3-chronicle.googleapis.com`
  * `europe-west6-chronicle.googleapis.com`
  * `europe-west9-chronicle.googleapis.com`
  * `europe-west12-chronicle.googleapis.com`
  * `me-central1-chronicle.googleapis.com`
  * `me-central2-chronicle.googleapis.com`
  * `me-west1-chronicle.googleapis.com`
  * `northamerica-northeast2-chronicle.googleapis.com`
  * `southamerica-east1-chronicle.googleapis.com`
  * `us-chronicle.googleapis.com`

  
Regional API endpoints: 

  * `chronicle.africa-south1.rep.googleapis.com`
  * `chronicle.asia-northeast1.rep.googleapis.com`
  * `chronicle.asia-south1.rep.googleapis.com`
  * `chronicle.asia-southeast1.rep.googleapis.com`
  * `chronicle.asia-southeast2.rep.googleapis.com`
  * `chronicle.australia-southeast1.rep.googleapis.com`
  * `chronicle.eu.rep.googleapis.com`
  * `chronicle.europe-west2.rep.googleapis.com`
  * `chronicle.europe-west3.rep.googleapis.com`
  * `chronicle.europe-west6.rep.googleapis.com`
  * `chronicle.europe-west9.rep.googleapis.com`
  * `chronicle.europe-west12.rep.googleapis.com`
  * `chronicle.me-central1.rep.googleapis.com`
  * `chronicle.me-central2.rep.googleapis.com`
  * `chronicle.me-west1.rep.googleapis.com`
  * `chronicle.northamerica-northeast2.rep.googleapis.com`
  * `chronicle.southamerica-east1.rep.googleapis.com`
  * `chronicle.us.rep.googleapis.com`

  
|  None   
Google Workspace add-ons  |  Global API endpoints: 

  * `gsuiteaddons.googleapis.com`

  
|  None   
Identity and Access Management  |  Global API endpoints: 

  * `iam.googleapis.com`

  
|  None   
Identity-Aware Proxy  |  Global API endpoints: 

  * `iap.googleapis.com`

  
|  None   
Image streaming  |  Global API endpoints: 

  * `containerfilesystem.googleapis.com`

  
|  None   
Immersive Stream  |  Global API endpoints: 

  * `stream.googleapis.com`

  
|  None   
Infrastructure Manager  |  Global API endpoints: 

  * `config.googleapis.com`

  
|  None   
Integration Connectors  |  Global API endpoints: 

  * `connectors.googleapis.com`

  
|  None   
KRM API Hosting  |  Global API endpoints: 

  * `krmapihosting.googleapis.com`

  
|  None   
Live Stream API  |  Global API endpoints: 

  * `livestream.googleapis.com`

  
|  None   
Looker API  |  Global API endpoints: 

  * `looker.googleapis.com`

  
|  None   
AlloyDB for PostgreSQL  |  Global API endpoints: 

  * `alloydb.googleapis.com`

  
|  None   
BigQuery Engine for Apache Flink  |  Global API endpoints: 

  * `managedflink.googleapis.com`

  
|  None   
Managed Kafka API  |  Global API endpoints: 

  * `managedkafka.googleapis.com`

  
|  None   
Google Cloud Managed Lustre  |  Global API endpoints: 

  * `lustre.googleapis.com`

  
|  None   
Media Asset Manager  |  Global API endpoints: 

  * `mediaasset.googleapis.com`

  
|  None   
Memorystore for Memcached  |  Global API endpoints: 

  * `memcache.googleapis.com`

  
|  None   
Memorystore for Redis  |  Global API endpoints: 

  * `redis.googleapis.com`

  
|  None   
Memorystore for Valkey  |  Global API endpoints: 

  * `memorystore.googleapis.com`

  
|  None   
Microservices API  |  Global API endpoints: 

  * `microservices.googleapis.com`

  
|  None   
Model Armor  |  Global API endpoints: 

  * `modelarmor.googleapis.com`

  
|  None   
Network Connectivity Center  |  Global API endpoints: 

  * `networkconnectivity.googleapis.com`

  
|  None   
NCC Gateway  |  Global API endpoints: 

  * `networkconnectivity.googleapis.com`
  * `networksecurity.googleapis.com`

  
|  None   
Network Intelligence Center  |  Global API endpoints: 

  * `networkmanagement.googleapis.com`

  
|  None   
Network Service Tiers  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Persistent Disk  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Oracle Database@Google Cloud  |  Global API endpoints: 

  * `oracledatabase.googleapis.com`

  
|  None   
Parallelstore  |  Global API endpoints: 

  * `parallelstore.googleapis.com`

  
|  None   
Parameter Manager  |  Global API endpoints: 

  * `parametermanager.googleapis.com`

  
|  None   
Policy Analyzer  |  Global API endpoints: 

  * `policyanalyzer.googleapis.com`

  
|  None   
Policy Troubleshooter  |  Global API endpoints: 

  * `policytroubleshooter.googleapis.com`

  
|  None   
Privileged Access Manager  |  Global API endpoints: 

  * `privilegedaccessmanager.googleapis.com`

  
|  None   
Progressive Rollout  |  Global API endpoints: 

  * `progressiverollout.googleapis.com`

  
|  None   
Pub/Sub  |  Global API endpoints: 

  * `pubsub.googleapis.com`

  
|  None   
Public Certificate Authority  |  Global API endpoints: 

  * `publicca.googleapis.com`

  
|  None   
Recommender  |  Global API endpoints: 

  * `recommender.googleapis.com`

  
|  None   
Remote Build Execution  |  Global API endpoints: 

  * `remotebuildexecution.googleapis.com`

  
|  None   
AI Commerce Search API  |  Global API endpoints: 

  * `retail.googleapis.com`

  
|  None   
Cyber Insurance Hub  |  Global API endpoints: 

  * `riskmanager.googleapis.com`

  
|  None   
SaaS Service Management API  |  Global API endpoints: 

  * `saasservicemgmt.googleapis.com`

  
|  None   
SecLM API  |  Global API endpoints: 

  * `seclm.googleapis.com`

  
|  None   
Secret Manager  |  Global API endpoints: 

  * `secretmanager.googleapis.com`

  
|  None   
Secure Source Manager  |  Global API endpoints: 

  * `securesourcemanager.googleapis.com`

  
|  None   
Secure Web Proxy  |  Global API endpoints: 

  * `networksecurity.googleapis.com`
  * `networkservices.googleapis.com`

  
|  None   
Security Command Center  |  Global API endpoints: 

  * `securitycenter.googleapis.com`
  * `securitycentermanagement.googleapis.com`
  * `securityposture.googleapis.com`

  
|  None   
Sensitive Data Protection  |  Global API endpoints: 

  * `dlp.googleapis.com`

  
|  None   
Service Account Credentials API  |  Global API endpoints: 

  * `iamcredentials.googleapis.com`

  
|  None   
Service Directory  |  Global API endpoints: 

  * `servicedirectory.googleapis.com`

  
|  None   
Personalized Service Health  |  Global API endpoints: 

  * `servicehealth.googleapis.com`

  
|  None   
Service Networking  |  Global API endpoints: 

  * `servicenetworking.googleapis.com`

  
|  None   
Service Usage  |  Global API endpoints: 

  * `serviceusage.googleapis.com`

  
|  None   
Speaker ID  |  Global API endpoints: 

  * `speakerid.googleapis.com`

  
|  None   
Speech-to-Text  |  Global API endpoints: 

  * `speech.googleapis.com`

  
  
Locational API endpoints: 

  * `asia-northeast1-speech.googleapis.com`
  * `asia-northeast3-speech.googleapis.com`
  * `asia-south1-speech.googleapis.com`
  * `asia-southeast1-speech.googleapis.com`
  * `australia-southeast1-speech.googleapis.com`
  * `europe-west1-speech.googleapis.com`
  * `europe-west2-speech.googleapis.com`
  * `europe-west3-speech.googleapis.com`
  * `europe-west4-speech.googleapis.com`
  * `northamerica-northeast1-speech.googleapis.com`
  * `southamerica-east1-speech.googleapis.com`
  * `us-central1-speech.googleapis.com`
  * `us-east1-speech.googleapis.com`
  * `us-east4-speech.googleapis.com`
  * `us-west1-speech.googleapis.com`

  
|  None   
Storage Insights  |  Global API endpoints: 

  * `storageinsights.googleapis.com`

  
|  None   
Storage Transfer Service  |  Global API endpoints: 

  * `storagebatchoperations.googleapis.com`
  * `storagetransfer.googleapis.com`

  
|  None   
Text-to-Speech  |  Global API endpoints: 

  * `texttospeech.googleapis.com`

  
|  None   
Timeseries Insights API  |  Global API endpoints: 

  * `timeseriesinsights.googleapis.com`

  
|  None   
Transcoder API  |  Global API endpoints: 

  * `transcoder.googleapis.com`

  
|  None   
Transfer Appliance  |  Global API endpoints: 

  * `transferappliance.googleapis.com`

  
|  None   
VM Manager  |  Global API endpoints: 

  * `osconfig.googleapis.com`

  
|  None   
Agent Platform API  |  Global API endpoints: 

  * `aiplatform.googleapis.com`

  
  
Locational API endpoints: 

  * `africa-south1-aiplatform.googleapis.com`
  * `asia-east1-aiplatform.googleapis.com`
  * `asia-east2-aiplatform.googleapis.com`
  * `asia-northeast1-aiplatform.googleapis.com`
  * `asia-northeast2-aiplatform.googleapis.com`
  * `asia-northeast3-aiplatform.googleapis.com`
  * `asia-south1-aiplatform.googleapis.com`
  * `asia-south2-aiplatform.googleapis.com`
  * `asia-southeast1-aiplatform.googleapis.com`
  * `asia-southeast2-aiplatform.googleapis.com`
  * `australia-southeast1-aiplatform.googleapis.com`
  * `australia-southeast2-aiplatform.googleapis.com`
  * `eu-aiplatform.googleapis.com`
  * `europe-central2-aiplatform.googleapis.com`
  * `europe-north1-aiplatform.googleapis.com`
  * `europe-north2-aiplatform.googleapis.com`
  * `europe-southwest1-aiplatform.googleapis.com`
  * `europe-west1-aiplatform.googleapis.com`
  * `europe-west2-aiplatform.googleapis.com`
  * `europe-west3-aiplatform.googleapis.com`
  * `europe-west4-aiplatform.googleapis.com`
  * `europe-west6-aiplatform.googleapis.com`
  * `europe-west8-aiplatform.googleapis.com`
  * `europe-west9-aiplatform.googleapis.com`
  * `europe-west10-aiplatform.googleapis.com`
  * `europe-west12-aiplatform.googleapis.com`
  * `me-central1-aiplatform.googleapis.com`
  * `me-central2-aiplatform.googleapis.com`
  * `me-west1-aiplatform.googleapis.com`
  * `northamerica-northeast1-aiplatform.googleapis.com`
  * `northamerica-northeast2-aiplatform.googleapis.com`
  * `southamerica-east1-aiplatform.googleapis.com`
  * `southamerica-west1-aiplatform.googleapis.com`
  * `us-aiplatform.googleapis.com`
  * `us-central1-aiplatform.googleapis.com`
  * `us-east1-aiplatform.googleapis.com`
  * `us-east4-aiplatform.googleapis.com`
  * `us-east5-aiplatform.googleapis.com`
  * `us-south1-aiplatform.googleapis.com`
  * `us-west1-aiplatform.googleapis.com`
  * `us-west2-aiplatform.googleapis.com`
  * `us-west3-aiplatform.googleapis.com`
  * `us-west4-aiplatform.googleapis.com`
  * `us-west8-aiplatform.googleapis.com`

  
Regional API endpoints: 

  * `aiplatform.africa-south1.rep.googleapis.com`
  * `aiplatform.asia-east1.rep.googleapis.com`
  * `aiplatform.asia-east2.rep.googleapis.com`
  * `aiplatform.asia-northeast1.rep.googleapis.com`
  * `aiplatform.asia-northeast2.rep.googleapis.com`
  * `aiplatform.asia-northeast3.rep.googleapis.com`
  * `aiplatform.asia-south1.rep.googleapis.com`
  * `aiplatform.asia-south2.rep.googleapis.com`
  * `aiplatform.asia-southeast1.rep.googleapis.com`
  * `aiplatform.asia-southeast2.rep.googleapis.com`
  * `aiplatform.australia-southeast1.rep.googleapis.com`
  * `aiplatform.australia-southeast2.rep.googleapis.com`
  * `aiplatform.eu.rep.googleapis.com`
  * `aiplatform.europe-central2.rep.googleapis.com`
  * `aiplatform.europe-north1.rep.googleapis.com`
  * `aiplatform.europe-north2.rep.googleapis.com`
  * `aiplatform.europe-southwest1.rep.googleapis.com`
  * `aiplatform.europe-west1.rep.googleapis.com`
  * `aiplatform.europe-west2.rep.googleapis.com`
  * `aiplatform.europe-west3.rep.googleapis.com`
  * `aiplatform.europe-west4.rep.googleapis.com`
  * `aiplatform.europe-west6.rep.googleapis.com`
  * `aiplatform.europe-west8.rep.googleapis.com`
  * `aiplatform.europe-west9.rep.googleapis.com`
  * `aiplatform.europe-west10.rep.googleapis.com`
  * `aiplatform.europe-west12.rep.googleapis.com`
  * `aiplatform.me-central1.rep.googleapis.com`
  * `aiplatform.me-central2.rep.googleapis.com`
  * `aiplatform.me-west1.rep.googleapis.com`
  * `aiplatform.northamerica-northeast1.rep.googleapis.com`
  * `aiplatform.northamerica-northeast2.rep.googleapis.com`
  * `aiplatform.southamerica-east1.rep.googleapis.com`
  * `aiplatform.southamerica-west1.rep.googleapis.com`
  * `aiplatform.us-central1.rep.googleapis.com`
  * `aiplatform.us-east1.rep.googleapis.com`
  * `aiplatform.us-east4.rep.googleapis.com`
  * `aiplatform.us-east5.rep.googleapis.com`
  * `aiplatform.us-south1.rep.googleapis.com`
  * `aiplatform.us-west1.rep.googleapis.com`
  * `aiplatform.us-west2.rep.googleapis.com`
  * `aiplatform.us-west3.rep.googleapis.com`
  * `aiplatform.us-west4.rep.googleapis.com`
  * `aiplatform.us-west8.rep.googleapis.com`
  * `aiplatform.us.rep.googleapis.com`

  
|  Shares underlying API endpoints with Generative AI on Gemini Enterprise Agent Platform and Vector Search. Endpoint restrictions applied to these endpoints affect all Vertex AI services. You can also manage access using the curated `in:*-aiplatform-endpoints` value groups (such as `in:global-aiplatform-endpoints`, `in:aiplatform-us-endpoints`, and `in:non-us-aiplatform-endpoints`).   
Vector Search  |  Global API endpoints: 

  * `aiplatform.googleapis.com`

  
  
Locational API endpoints: 

  * `africa-south1-aiplatform.googleapis.com`
  * `asia-east1-aiplatform.googleapis.com`
  * `asia-east2-aiplatform.googleapis.com`
  * `asia-northeast1-aiplatform.googleapis.com`
  * `asia-northeast2-aiplatform.googleapis.com`
  * `asia-northeast3-aiplatform.googleapis.com`
  * `asia-south1-aiplatform.googleapis.com`
  * `asia-south2-aiplatform.googleapis.com`
  * `asia-southeast1-aiplatform.googleapis.com`
  * `asia-southeast2-aiplatform.googleapis.com`
  * `australia-southeast1-aiplatform.googleapis.com`
  * `australia-southeast2-aiplatform.googleapis.com`
  * `eu-aiplatform.googleapis.com`
  * `europe-central2-aiplatform.googleapis.com`
  * `europe-north1-aiplatform.googleapis.com`
  * `europe-north2-aiplatform.googleapis.com`
  * `europe-southwest1-aiplatform.googleapis.com`
  * `europe-west1-aiplatform.googleapis.com`
  * `europe-west2-aiplatform.googleapis.com`
  * `europe-west3-aiplatform.googleapis.com`
  * `europe-west4-aiplatform.googleapis.com`
  * `europe-west6-aiplatform.googleapis.com`
  * `europe-west8-aiplatform.googleapis.com`
  * `europe-west9-aiplatform.googleapis.com`
  * `europe-west10-aiplatform.googleapis.com`
  * `europe-west12-aiplatform.googleapis.com`
  * `me-central1-aiplatform.googleapis.com`
  * `me-central2-aiplatform.googleapis.com`
  * `me-west1-aiplatform.googleapis.com`
  * `northamerica-northeast1-aiplatform.googleapis.com`
  * `northamerica-northeast2-aiplatform.googleapis.com`
  * `southamerica-east1-aiplatform.googleapis.com`
  * `southamerica-west1-aiplatform.googleapis.com`
  * `us-aiplatform.googleapis.com`
  * `us-central1-aiplatform.googleapis.com`
  * `us-east1-aiplatform.googleapis.com`
  * `us-east4-aiplatform.googleapis.com`
  * `us-east5-aiplatform.googleapis.com`
  * `us-south1-aiplatform.googleapis.com`
  * `us-west1-aiplatform.googleapis.com`
  * `us-west2-aiplatform.googleapis.com`
  * `us-west3-aiplatform.googleapis.com`
  * `us-west4-aiplatform.googleapis.com`
  * `us-west8-aiplatform.googleapis.com`

  
Regional API endpoints: 

  * `aiplatform.africa-south1.rep.googleapis.com`
  * `aiplatform.asia-east1.rep.googleapis.com`
  * `aiplatform.asia-east2.rep.googleapis.com`
  * `aiplatform.asia-northeast1.rep.googleapis.com`
  * `aiplatform.asia-northeast2.rep.googleapis.com`
  * `aiplatform.asia-northeast3.rep.googleapis.com`
  * `aiplatform.asia-south1.rep.googleapis.com`
  * `aiplatform.asia-south2.rep.googleapis.com`
  * `aiplatform.asia-southeast1.rep.googleapis.com`
  * `aiplatform.asia-southeast2.rep.googleapis.com`
  * `aiplatform.australia-southeast1.rep.googleapis.com`
  * `aiplatform.australia-southeast2.rep.googleapis.com`
  * `aiplatform.eu.rep.googleapis.com`
  * `aiplatform.europe-central2.rep.googleapis.com`
  * `aiplatform.europe-north1.rep.googleapis.com`
  * `aiplatform.europe-north2.rep.googleapis.com`
  * `aiplatform.europe-southwest1.rep.googleapis.com`
  * `aiplatform.europe-west1.rep.googleapis.com`
  * `aiplatform.europe-west2.rep.googleapis.com`
  * `aiplatform.europe-west3.rep.googleapis.com`
  * `aiplatform.europe-west4.rep.googleapis.com`
  * `aiplatform.europe-west6.rep.googleapis.com`
  * `aiplatform.europe-west8.rep.googleapis.com`
  * `aiplatform.europe-west9.rep.googleapis.com`
  * `aiplatform.europe-west10.rep.googleapis.com`
  * `aiplatform.europe-west12.rep.googleapis.com`
  * `aiplatform.me-central1.rep.googleapis.com`
  * `aiplatform.me-central2.rep.googleapis.com`
  * `aiplatform.me-west1.rep.googleapis.com`
  * `aiplatform.northamerica-northeast1.rep.googleapis.com`
  * `aiplatform.northamerica-northeast2.rep.googleapis.com`
  * `aiplatform.southamerica-east1.rep.googleapis.com`
  * `aiplatform.southamerica-west1.rep.googleapis.com`
  * `aiplatform.us-central1.rep.googleapis.com`
  * `aiplatform.us-east1.rep.googleapis.com`
  * `aiplatform.us-east4.rep.googleapis.com`
  * `aiplatform.us-east5.rep.googleapis.com`
  * `aiplatform.us-south1.rep.googleapis.com`
  * `aiplatform.us-west1.rep.googleapis.com`
  * `aiplatform.us-west2.rep.googleapis.com`
  * `aiplatform.us-west3.rep.googleapis.com`
  * `aiplatform.us-west4.rep.googleapis.com`
  * `aiplatform.us-west8.rep.googleapis.com`
  * `aiplatform.us.rep.googleapis.com`

  
|  Shares underlying API endpoints with Gemini Enterprise Agent Platform and Generative AI on Gemini Enterprise Agent Platform. Endpoint restrictions applied to these endpoints affect all Vertex AI services. You can also manage access using the curated `in:*-aiplatform-endpoints` value groups (such as `in:global-aiplatform-endpoints`, `in:aiplatform-us-endpoints`, and `in:non-us-aiplatform-endpoints`).   
Gemini Enterprise Agent Platform Workbench  |  Global API endpoints: 

  * `notebooks.googleapis.com`

  
|  None   
Video Search API  |  Global API endpoints: 

  * `cloudvideosearch.googleapis.com`

  
|  None   
Video Stitcher API  |  Global API endpoints: 

  * `videostitcher.googleapis.com`

  
|  None   
Cloud Vision  |  Global API endpoints: 

  * `vision.googleapis.com`

  
  
Locational API endpoints: 

  * `eu-vision.googleapis.com`
  * `us-vision.googleapis.com`

  
|  None   
Virtual Private Cloud (VPC)  |  Global API endpoints: 

  * `compute.googleapis.com`

  
|  None   
Web Risk  |  Global API endpoints: 

  * `webrisk.googleapis.com`

  
|  None   
Web Security Scanner  |  Global API endpoints: 

  * `websecurityscanner.googleapis.com`

  
|  None   
Workflows  |  Global API endpoints: 

  * `workflows.googleapis.com`
  * `workflowexecutions.googleapis.com`

  
  
Locational API endpoints: 

  * `africa-south1-workflowexecutions.googleapis.com`
  * `asia-east1-workflowexecutions.googleapis.com`
  * `asia-east2-workflowexecutions.googleapis.com`
  * `asia-northeast1-workflowexecutions.googleapis.com`
  * `asia-northeast2-workflowexecutions.googleapis.com`
  * `asia-northeast3-workflowexecutions.googleapis.com`
  * `asia-south1-workflowexecutions.googleapis.com`
  * `asia-south2-workflowexecutions.googleapis.com`
  * `asia-southeast1-workflowexecutions.googleapis.com`
  * `asia-southeast2-workflowexecutions.googleapis.com`
  * `australia-southeast1-workflowexecutions.googleapis.com`
  * `australia-southeast2-workflowexecutions.googleapis.com`
  * `europe-central2-workflowexecutions.googleapis.com`
  * `europe-north1-workflowexecutions.googleapis.com`
  * `europe-southwest1-workflowexecutions.googleapis.com`
  * `europe-west1-workflowexecutions.googleapis.com`
  * `europe-west2-workflowexecutions.googleapis.com`
  * `europe-west3-workflowexecutions.googleapis.com`
  * `europe-west4-workflowexecutions.googleapis.com`
  * `europe-west6-workflowexecutions.googleapis.com`
  * `europe-west8-workflowexecutions.googleapis.com`
  * `europe-west9-workflowexecutions.googleapis.com`
  * `europe-west10-workflowexecutions.googleapis.com`
  * `europe-west12-workflowexecutions.googleapis.com`
  * `me-central1-workflowexecutions.googleapis.com`
  * `me-central2-workflowexecutions.googleapis.com`
  * `me-west1-workflowexecutions.googleapis.com`
  * `northamerica-northeast1-workflowexecutions.googleapis.com`
  * `northamerica-northeast2-workflowexecutions.googleapis.com`
  * `southamerica-east1-workflowexecutions.googleapis.com`
  * `southamerica-west1-workflowexecutions.googleapis.com`
  * `us-central1-workflowexecutions.googleapis.com`
  * `us-east1-workflowexecutions.googleapis.com`
  * `us-east4-workflowexecutions.googleapis.com`
  * `us-east5-workflowexecutions.googleapis.com`
  * `us-south1-workflowexecutions.googleapis.com`
  * `us-west1-workflowexecutions.googleapis.com`
  * `us-west2-workflowexecutions.googleapis.com`
  * `us-west3-workflowexecutions.googleapis.com`
  * `us-west4-workflowexecutions.googleapis.com`

  
|  None   
Workload Certificate API  |  Global API endpoints: 

  * `workloadcertificate.googleapis.com`

  
|  None   
Workload Manager  |  Global API endpoints: 

  * `workloadmanager.googleapis.com`

  
|  None   
  
## Value groups

Value groups are collections of groups and API endpoints that are curated by Google to provide a simpler way to define your endpoint restrictions. Value groups include many related API endpoints and are expanded over time by Google without needing to change your organization policy to accommodate the new endpoints.

To use value groups in your organization policy, prefix your entries with the string `in:`. For more information on using value prefixes, see [Using Constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#hierarchy_subtree). Group names are validated on the call to set the organization policy. Using an invalid group name will cause the policy setting to fail.

The following table contains the current list of available groups:

Group | Details | Direct members  
---|---|---  
global-accessapproval-endpoints  |  Access Approval global API endpoints:  
`in:global-accessapproval-endpoints` | _Values:_  


  * `accessapproval.googleapis.com`
  * `accessapproval.mtls.googleapis.com`
  * `content-accessapproval.googleapis.com`
  * `content-accessapproval.mtls.googleapis.com`

  
global-accesscontextintelligence-endpoints  |  Access Context Intelligence global API Endpoints:  
`in:global-accesscontextintelligence-endpoints` | _Values:_  


  * `accesscontextintelligence.googleapis.com`
  * `accesscontextintelligence.mtls.googleapis.com`
  * `content-accesscontextintelligence.googleapis.com`
  * `content-accesscontextintelligence.mtls.googleapis.com`

  
global-agentidentity-endpoints  |  Agent Identity global API Endpoints:  
`in:global-agentidentity-endpoints` | _Values:_  


  * `agentidentity.googleapis.com`
  * `agentidentity.mtls.googleapis.com`
  * `content-agentidentity.googleapis.com`
  * `content-agentidentity.mtls.googleapis.com`

  
global-agentidentitycredentials-endpoints  |  Agent Identity Credentials global API Endpoints:  
`in:global-agentidentitycredentials-endpoints` | _Values:_  


  * `agentidentitycredentials.googleapis.com`
  * `agentidentitycredentials.mtls.googleapis.com`
  * `content-agentidentitycredentials.googleapis.com`
  * `content-agentidentitycredentials.mtls.googleapis.com`

  
global-agentregistry-endpoints  |  Agent Registry global API Endpoints:  
`in:global-agentregistry-endpoints` | _Values:_  


  * `agentregistry.googleapis.com`
  * `agentregistry.mtls.googleapis.com`
  * `content-agentregistry.googleapis.com`
  * `content-agentregistry.mtls.googleapis.com`

  
global-agentregistryendpoint-endpoints  |  Agent Registry global API Endpoints:  
`in:global-agentregistryendpoint-endpoints` | _Values:_  


  * `agentregistryendpoint.googleapis.com`
  * `agentregistryendpoint.mtls.googleapis.com`
  * `content-agentregistryendpoint.googleapis.com`
  * `content-agentregistryendpoint.mtls.googleapis.com`

  
global-alloydb-endpoints  |  AlloyDB global API endpoints:  
`in:global-alloydb-endpoints` | _Values:_  


  * `alloydb.googleapis.com`
  * `alloydb.mtls.googleapis.com`
  * `content-alloydb.googleapis.com`
  * `content-alloydb.mtls.googleapis.com`

  
global-anthosidentityservice-endpoints  |  Anthos Identity Service global API endpoints:  
`in:global-anthosidentityservice-endpoints` | _Values:_  


  * `anthosidentityservice.googleapis.com`

  
global-apigee-endpoints  |  Apigee global API Endpoints:  
`in:global-apigee-endpoints` | _Values:_  


  * `apigee.googleapis.com`
  * `apigee.mtls.googleapis.com`
  * `content-apigee.googleapis.com`
  * `content-apigee.mtls.googleapis.com`

  
global-apikeys-endpoints  |  API keys global API Endpoints:  
`in:global-apikeys-endpoints` | _Values:_  


  * `apikeys.googleapis.com`
  * `apikeys.mtls.googleapis.com`
  * `content-apikeys.googleapis.com`
  * `content-apikeys.mtls.googleapis.com`

  
global-apphub-endpoints  |  App Hub global API endpoints:  
`in:global-apphub-endpoints` | _Values:_  


  * `apphub.googleapis.com`
  * `apphub.mtls.googleapis.com`
  * `content-apphub.googleapis.com`
  * `content-apphub.mtls.googleapis.com`

  
global-artifactregistry-endpoints  |  Artifact Registry global API endpoints:  
`in:global-artifactregistry-endpoints` | _Values:_  


  * `artifactregistry.googleapis.com`
  * `artifactregistry.mtls.googleapis.com`
  * `content-artifactregistry.googleapis.com`
  * `content-artifactregistry.mtls.googleapis.com`

  
global-auditmanager-endpoints  |  Audit Manager global API Endpoints:  
`in:global-auditmanager-endpoints` | _Values:_  


  * `auditmanager.googleapis.com`
  * `auditmanager.mtls.googleapis.com`
  * `content-auditmanager.googleapis.com`
  * `content-auditmanager.mtls.googleapis.com`

  
global-backupdr-endpoints  |  Backup and DR global API endpoints:  
`in:global-backupdr-endpoints` | _Values:_  


  * `backupdr.googleapis.com`
  * `backupdr.mtls.googleapis.com`
  * `content-backupdr.googleapis.com`
  * `content-backupdr.mtls.googleapis.com`

  
global-bigquery-connections-endpoints  |  BigQuery Connections global API endpoints:  
`in:global-bigquery-connections-endpoints` | _Values:_  


  * `bigqueryconnection.googleapis.com`
  * `bigqueryconnection.mtls.googleapis.com`
  * `content-bigqueryconnection.googleapis.com`
  * `content-bigqueryconnection.mtls.googleapis.com`

  
global-bigquery-datapolicy-endpoints  |  BigQuery Data Policy global API endpoints:  
`in:global-bigquery-datapolicy-endpoints` | _Values:_  


  * `bigquerydatapolicy.googleapis.com`
  * `bigquerydatapolicy.mtls.googleapis.com`
  * `content-bigquerydatapolicy.googleapis.com`
  * `content-bigquerydatapolicy.mtls.googleapis.com`

  
global-bigquery-datatransfer-endpoints  |  BigQuery Data Transfer global API endpoints:  
`in:global-bigquery-datatransfer-endpoints` | _Values:_  


  * `bigquerydatatransfer.googleapis.com`
  * `bigquerydatatransfer.mtls.googleapis.com`
  * `content-bigquerydatatransfer.googleapis.com`
  * `content-bigquerydatatransfer.mtls.googleapis.com`

  
global-bigquery-migration-endpoints  |  BigQuery Migration global API endpoints:  
`in:global-bigquery-migration-endpoints` | _Values:_  


  * `bigquerymigration.googleapis.com`
  * `bigquerymigration.mtls.googleapis.com`
  * `content-bigquerymigration.googleapis.com`
  * `content-bigquerymigration.mtls.googleapis.com`

  
global-bigtable-endpoints  |  Cloud Bigtable global API endpoints:  
`in:global-bigtable-endpoints` | _Values:_  


  * `bigtable.googleapis.com`
  * `bigtableadmin.googleapis.com`

  
global-binaryauthorization-endpoints  |  Binary Authorization global API endpoints:  
`in:global-binaryauthorization-endpoints` | _Values:_  


  * `binaryauthorization.googleapis.com`
  * `binaryauthorization.mtls.googleapis.com`
  * `content-binaryauthorization.googleapis.com`
  * `content-binaryauthorization.mtls.googleapis.com`

  
global-cas-endpoints  |  Certificate Authority Service global API endpoints:  
`in:global-cas-endpoints` | _Values:_  


  * `content-privateca.googleapis.com`
  * `content-privateca.mtls.googleapis.com`
  * `privateca.googleapis.com`
  * `privateca.mtls.googleapis.com`

  
global-certificatemanager-endpoints  |  Certificate Manager global API endpoints:  
`in:global-certificatemanager-endpoints` | _Values:_  


  * `certificatemanager.googleapis.com`
  * `certificatemanager.mtls.googleapis.com`

  
global-cloudasset-endpoints  |  Cloud Asset Inventory global API Endpoints:  
`in:global-cloudasset-endpoints` | _Values:_  


  * `cloudasset.googleapis.com`
  * `cloudasset.mtls.googleapis.com`
  * `content-cloudasset.googleapis.com`
  * `content-cloudasset.mtls.googleapis.com`

  
global-cloudbilling-endpoints  |  Cloud Billing global API endpoints:  
`in:global-cloudbilling-endpoints` | _Values:_  


  * `cloudbilling.googleapis.com`
  * `cloudbilling.mtls.googleapis.com`
  * `content-cloudbilling.googleapis.com`
  * `content-cloudbilling.mtls.googleapis.com`

  
global-cloudbuild-endpoints  |  Cloud Build global API endpoints:  
`in:global-cloudbuild-endpoints` | _Values:_  


  * `cloudbuild.googleapis.com`
  * `cloudbuild.mtls.googleapis.com`
  * `content-cloudbuild.googleapis.com`

  
global-cloudquotas-endpoints  |  Cloud Quotas global API Endpoints:  
`in:global-cloudquotas-endpoints` | _Values:_  


  * `cloudquotas.googleapis.com`
  * `cloudquotas.mtls.googleapis.com`
  * `content-cloudquotas.googleapis.com`
  * `content-cloudquotas.mtls.googleapis.com`

  
global-cloudscheduler-endpoints  |  Cloud Scheduler global API endpoints:  
`in:global-cloudscheduler-endpoints` | _Values:_  


  * `cloudscheduler.googleapis.com`
  * `cloudscheduler.mtls.googleapis.com`
  * `content-cloudscheduler.googleapis.com`
  * `content-cloudscheduler.mtls.googleapis.com`

  
global-cloudsecuritycompliance-endpoints  |  Compliance Manager global API endpoints:  
`in:global-cloudsecuritycompliance-endpoints` | _Values:_  


  * `cloudsecuritycompliance.googleapis.com`
  * `cloudsecuritycompliance.mtls.googleapis.com`
  * `content-cloudsecuritycompliance.googleapis.com`
  * `content-cloudsecuritycompliance.mtls.googleapis.com`

  
global-cloudtasks-endpoints  |  Cloud Tasks global API endpoints:  
`in:global-cloudtasks-endpoints` | _Values:_  


  * `cloudtasks.googleapis.com`
  * `cloudtasks.mtls.googleapis.com`
  * `content-cloudtasks.googleapis.com`
  * `content-cloudtasks.mtls.googleapis.com`

  
global-cloudtrace-endpoints  |  Cloud Trace global API Endpoints:  
`in:global-cloudtrace-endpoints` | _Values:_  


  * `cloudtrace.googleapis.com`
  * `cloudtrace.mtls.googleapis.com`
  * `content-cloudtrace.googleapis.com`
  * `content-cloudtrace.mtls.googleapis.com`

  
global-composer-endpoints  |  Cloud Composer global API endpoints:  
`in:global-composer-endpoints` | _Values:_  


  * `composer.googleapis.com`

  
global-compute-endpoints  |  Cloud Compute Engine global API endpoints:  
`in:global-compute-endpoints` | _Values:_  


  * `compute.googleapis.com`
  * `compute.mtls.googleapis.com`
  * `content-compute.googleapis.com`
  * `content-compute.mtls.googleapis.com`

  
global-config-endpoints  |  Config global API endpoints:  
`in:global-config-endpoints` | _Values:_  


  * `config.googleapis.com`
  * `config.mtls.googleapis.com`
  * `content-config.googleapis.com`
  * `content-config.mtls.googleapis.com`

  
global-connectgateway-endpoints  |  Connect Gateway global API endpoints:  
`in:global-connectgateway-endpoints` | _Values:_  


  * `connectgateway.googleapis.com`
  * `connectgateway.mtls.googleapis.com`
  * `content-connectgateway.googleapis.com`
  * `content-connectgateway.mtls.googleapis.com`

  
global-connectors-endpoints  |  Integration Connectors global API Endpoints:  
`in:global-connectors-endpoints` | _Values:_  


  * `connectors.googleapis.com`
  * `connectors.mtls.googleapis.com`
  * `content-connectors.googleapis.com`
  * `content-connectors.mtls.googleapis.com`

  
global-container-endpoints  |  Google Kubernetes Engine global API endpoints:  
`in:global-container-endpoints` | _Values:_  


  * `container.googleapis.com`
  * `container.mtls.googleapis.com`
  * `content-container.googleapis.com`
  * `content-container.mtls.googleapis.com`

  
global-containeranalysis-endpoints  |  Container Analysis global API endpoints:  
`in:global-containeranalysis-endpoints` | _Values:_  


  * `containeranalysis.googleapis.com`
  * `containeranalysis.mtls.googleapis.com`
  * `content-containeranalysis.googleapis.com`
  * `content-ondemandscanning.mtls.googleapis.com`
  * `ondemandscanning.googleapis.com`
  * `ondemandscanning.mtls.googleapis.com`

  
global-containerfilesystem-endpoints  |  Container Filesystem global API endpoints:  
`in:global-containerfilesystem-endpoints` | _Values:_  


  * `containerfilesystem.googleapis.com`
  * `containerfilesystem.mtls.googleapis.com`
  * `content-containerfilesystem.googleapis.com`
  * `content-containerfilesystem.mtls.googleapis.com`

  
global-containerthreatdetection-endpoints  |  Container Threat Detection Service global API endpoints:  
`in:global-containerthreatdetection-endpoints` | _Values:_  


  * `containerthreatdetection.googleapis.com`
  * `containerthreatdetection.mtls.googleapis.com`
  * `content-containerthreatdetection.googleapis.com`
  * `content-containerthreatdetection.mtls.googleapis.com`

  
global-databasecenter-endpoints  |  Database Center global API Endpoints:  
`in:global-databasecenter-endpoints` | _Values:_  


  * `content-databasecenter.googleapis.com`
  * `content-databasecenter.mtls.googleapis.com`
  * `databasecenter.googleapis.com`
  * `databasecenter.mtls.googleapis.com`

  
global-dataflow-endpoints  |  Dataflow global API endpoints:  
`in:global-dataflow-endpoints` | _Values:_  


  * `content-dataflow.googleapis.com`
  * `dataflow.googleapis.com`

  
global-dataform-endpoints  |  Dataform global API endpoints:  
`in:global-dataform-endpoints` | _Values:_  


  * `content-dataform.googleapis.com`
  * `content-dataform.mtls.googleapis.com`
  * `dataform.googleapis.com`
  * `dataform.mtls.googleapis.com`

  
global-datafusion-endpoints  |  Cloud Data Fusion global API endpoints:  
`in:global-datafusion-endpoints` | _Values:_  


  * `content-datafusion.googleapis.com`
  * `content-datafusion.mtls.googleapis.com`
  * `datafusion.googleapis.com`
  * `datafusion.mtls.googleapis.com`

  
global-datalineage-endpoints  |  Data Lineage global API endpoints:  
`in:global-datalineage-endpoints` | _Values:_  


  * `content-datalineage.googleapis.com`
  * `content-datalineage.mtls.googleapis.com`
  * `datalineage.googleapis.com`
  * `datalineage.mtls.googleapis.com`

  
global-dataplex-endpoints  |  Dataplex global API endpoints:  
`in:global-dataplex-endpoints` | _Values:_  


  * `content-dataplex.googleapis.com`
  * `content-dataplex.mtls.googleapis.com`
  * `dataplex.googleapis.com`
  * `dataplex.mtls.googleapis.com`

  
global-dataproc-endpoints  |  Cloud Dataproc global API endpoints:  
`in:global-dataproc-endpoints` | _Values:_  


  * `content-dataproc-control.googleapis.com`
  * `content-dataproc-control.mtls.googleapis.com`
  * `content-dataproc.googleapis.com`
  * `content-dataproc.mtls.googleapis.com`
  * `dataproc-control.googleapis.com`
  * `dataproc-control.mtls.googleapis.com`
  * `dataproc.googleapis.com`
  * `dataproc.mtls.googleapis.com`

  
global-datastore-endpoints  |  Firestore in Datastore mode global API endpoints:  
`in:global-datastore-endpoints` | _Values:_  


  * `content-datastore.googleapis.com`
  * `content-datastore.mtls.googleapis.com`
  * `datastore.googleapis.com`
  * `datastore.mtls.googleapis.com`

  
global-datastream-endpoints  |  Datastream global API Endpoints:  
`in:global-datastream-endpoints` | _Values:_  


  * `content-datastream.googleapis.com`
  * `content-datastream.mtls.googleapis.com`
  * `datastream.googleapis.com`
  * `datastream.mtls.googleapis.com`

  
global-developerconnect-endpoints  |  Developer Connect global API Endpoints:  
`in:global-developerconnect-endpoints` | _Values:_  


  * `content-developerconnect.googleapis.com`
  * `content-developerconnect.mtls.googleapis.com`
  * `developerconnect.googleapis.com`
  * `developerconnect.mtls.googleapis.com`

  
global-discoveryengine-endpoints  |  Vertex AI Search and Agentspace global API endpoints:  
`in:global-discoveryengine-endpoints` | _Values:_  


  * `content-discoveryengine.googleapis.com`
  * `content-discoveryengine.mtls.googleapis.com`
  * `discoveryengine.googleapis.com`
  * `discoveryengine.mtls.googleapis.com`

  
global-dlp-endpoints  |  Sensitive Data Protection DLP global API endpoints:  
`in:global-dlp-endpoints` | _Values:_  


  * `content-dlp.googleapis.com`
  * `dlp.googleapis.com`

  
global-dns-endpoints  |  Cloud DNS global API endpoints:  
`in:global-dns-endpoints` | _Values:_  


  * `content-dns.googleapis.com`
  * `content-dns.mtls.googleapis.com`
  * `dns.googleapis.com`
  * `dns.mtls.googleapis.com`

  
global-documentai-endpoints  |  Document AI global API endpoints:  
`in:global-documentai-endpoints` | _Values:_  


  * `content-documentai.googleapis.com`
  * `content-documentai.mtls.googleapis.com`
  * `documentai.googleapis.com`
  * `documentai.mtls.googleapis.com`

  
global-domains-endpoints  |  Cloud Domains global API Endpoints:  
`in:global-domains-endpoints` | _Values:_  


  * `content-domains.googleapis.com`
  * `content-domains.mtls.googleapis.com`
  * `domains.googleapis.com`
  * `domains.mtls.googleapis.com`

  
global-essentialcontacts-endpoints  |  Essential Contacts global API endpoints:  
`in:global-essentialcontacts-endpoints` | _Values:_  


  * `content-essentialcontacts.googleapis.com`
  * `content-essentialcontacts.mtls.googleapis.com`
  * `essentialcontacts.googleapis.com`
  * `essentialcontacts.mtls.googleapis.com`

  
global-eventarc-endpoints  |  Eventarc global API endpoints:  
`in:global-eventarc-endpoints` | _Values:_  


  * `content-eventarc.googleapis.com`
  * `content-eventarc.mtls.googleapis.com`
  * `eventarc.googleapis.com`
  * `eventarc.mtls.googleapis.com`

  
global-filestore-endpoints  |  Filestore global API endpoints:  
`in:global-filestore-endpoints` | _Values:_  


  * `content-file.googleapis.com`
  * `content-file.mtls.googleapis.com`
  * `file.googleapis.com`
  * `file.mtls.googleapis.com`

  
global-firebaserules-endpoints  |  Firebase Rules global API endpoints:  
`in:global-firebaserules-endpoints` | _Values:_  


  * `firebaserules.googleapis.com`

  
global-firestore-endpoints  |  Firestore global API endpoints:  
`in:global-firestore-endpoints` | _Values:_  


  * `content-firestore.googleapis.com`
  * `content-firestore.mtls.googleapis.com`
  * `firestore.googleapis.com`
  * `firestore.mtls.googleapis.com`

  
global-firestorekeyvisualizer-endpoints  |  Firestore Key Visualizer global API endpoints:  
`in:global-firestorekeyvisualizer-endpoints` | _Values:_  


  * `content-firestorekeyvisualizer.googleapis.com`
  * `content-firestorekeyvisualizer.mtls.googleapis.com`
  * `firestorekeyvisualizer.googleapis.com`
  * `firestorekeyvisualizer.mtls.googleapis.com`

  
global-gkebackup-endpoints  |  Backup for GKE global API endpoints:  
`in:global-gkebackup-endpoints` | _Values:_  


  * `content-gkebackup.googleapis.com`
  * `content-gkebackup.mtls.googleapis.com`
  * `gkebackup.googleapis.com`
  * `gkebackup.mtls.googleapis.com`

  
global-gkeconnect-endpoints  |  GKE Connect global API endpoints:  
`in:global-gkeconnect-endpoints` | _Values:_  


  * `content-gkeconnect.googleapis.com`
  * `content-gkeconnect.mtls.googleapis.com`
  * `gkeconnect.googleapis.com`
  * `gkeconnect.mtls.googleapis.com`

  
global-gkehub-endpoints  |  GKE Hub global API endpoints:  
`in:global-gkehub-endpoints` | _Values:_  


  * `content-gkehub.googleapis.com`
  * `content-gkehub.mtls.googleapis.com`
  * `gkehub.googleapis.com`
  * `gkehub.mtls.googleapis.com`

  
global-hypercomputecluster-endpoints  |  Cluster Director global API Endpoints:  
`in:global-hypercomputecluster-endpoints` | _Values:_  


  * `content-hypercomputecluster.googleapis.com`
  * `content-hypercomputecluster.mtls.googleapis.com`
  * `hypercomputecluster.googleapis.com`
  * `hypercomputecluster.mtls.googleapis.com`

  
global-iam-endpoints  |  Cloud IAM global API endpoints:  
`in:global-iam-endpoints` | _Values:_  


  * `content-iam.googleapis.com`
  * `content-iam.mtls.googleapis.com`
  * `iam.googleapis.com`
  * `iam.mtls.googleapis.com`

  
global-iap-endpoints  |  IAP global API endpoints:  
`in:global-iap-endpoints` | _Values:_  


  * `content-iap.googleapis.com`
  * `iap.googleapis.com`

  
global-kms-endpoints  |  Cloud Key Management Service global API endpoints:  
`in:global-kms-endpoints` | _Values:_  


  * `cloudkms.googleapis.com`
  * `cloudkms.mtls.googleapis.com`
  * `content-cloudkms.googleapis.com`
  * `content-cloudkms.mtls.googleapis.com`

  
global-looker-endpoints  |  Looker global API endpoints:  
`in:global-looker-endpoints` | _Values:_  


  * `content-looker.googleapis.com`
  * `content-looker.mtls.googleapis.com`
  * `looker.googleapis.com`
  * `looker.mtls.googleapis.com`

  
global-lustre-endpoints  |  Google Cloud Managed Lustre global API Endpoints:  
`in:global-lustre-endpoints` | _Values:_  


  * `content-lustre.googleapis.com`
  * `content-lustre.mtls.googleapis.com`
  * `lustre.googleapis.com`
  * `lustre.mtls.googleapis.com`

  
global-managedkafka-endpoints  |  Managed Kafka global API endpoints:  
`in:global-managedkafka-endpoints` | _Values:_  


  * `content-managedkafka.googleapis.com`
  * `content-managedkafka.mtls.googleapis.com`
  * `managedkafka.googleapis.com`
  * `managedkafka.mtls.googleapis.com`

  
global-memcache-endpoints  |  Memorystore for Memcache global API endpoints:  
`in:global-memcache-endpoints` | _Values:_  


  * `content-memcache.googleapis.com`
  * `content-memcache.mtls.googleapis.com`
  * `memcache.googleapis.com`
  * `memcache.mtls.googleapis.com`

  
global-memorystore-endpoints  |  Memorystore for Valkey global API endpoints:  
`in:global-memorystore-endpoints` | _Values:_  


  * `content-memorystore.googleapis.com`
  * `content-memorystore.mtls.googleapis.com`
  * `memorystore.googleapis.com`
  * `memorystore.mtls.googleapis.com`

  
global-meshconfig-endpoints  |  Mesh Configuration global API endpoints:  
`in:global-meshconfig-endpoints` | _Values:_  


  * `content-meshconfig.googleapis.com`
  * `content-meshconfig.mtls.googleapis.com`
  * `meshconfig.googleapis.com`
  * `meshconfig.mtls.googleapis.com`

  
global-migrationcenter-endpoints  |  Migration Center global API endpoints:  
`in:global-migrationcenter-endpoints` | _Values:_  


  * `content-migrationcenter.googleapis.com`
  * `content-migrationcenter.mtls.googleapis.com`
  * `migrationcenter.googleapis.com`
  * `migrationcenter.mtls.googleapis.com`

  
global-modelarmor-endpoints  |  Model Armor global API Endpoints:  
`in:global-modelarmor-endpoints` | _Values:_  


  * `content-modelarmor.googleapis.com`
  * `content-modelarmor.mtls.googleapis.com`
  * `modelarmor.googleapis.com`
  * `modelarmor.mtls.googleapis.com`

  
global-monitoring-endpoints  |  Cloud Monitoring global API endpoints:  
`in:global-monitoring-endpoints` | _Values:_  


  * `content-monitoring.googleapis.com`
  * `content-monitoring.mtls.googleapis.com`
  * `monitoring.googleapis.com`
  * `monitoring.mtls.googleapis.com`

  
global-netapp-endpoints  |  Google Cloud Netapp Volumes global API endpoints:  
`in:global-netapp-endpoints` | _Values:_  


  * `content-netapp.googleapis.com`
  * `content-netapp.mtls.googleapis.com`
  * `netapp.googleapis.com`
  * `netapp.mtls.googleapis.com`

  
global-networkconnectivity-endpoints  |  Network Connectivity global API endpoints:  
`in:global-networkconnectivity-endpoints` | _Values:_  


  * `content-networkconnectivity.googleapis.com`
  * `content-networkconnectivity.mtls.googleapis.com`
  * `networkconnectivity.googleapis.com`
  * `networkconnectivity.mtls.googleapis.com`

  
global-networkmanagement-endpoints  |  Connectivity Tests global API Endpoints:  
`in:global-networkmanagement-endpoints` | _Values:_  


  * `content-networkmanagement.googleapis.com`
  * `content-networkmanagement.mtls.googleapis.com`
  * `networkmanagement.googleapis.com`
  * `networkmanagement.mtls.googleapis.com`

  
global-networksecurity-endpoints  |  Network Security global API endpoints:  
`in:global-networksecurity-endpoints` | _Values:_  


  * `content-networksecurity.googleapis.com`
  * `content-networksecurity.mtls.googleapis.com`
  * `networksecurity.googleapis.com`
  * `networksecurity.mtls.googleapis.com`

  
global-networkservices-endpoints  |  Network Services global API endpoints:  
`in:global-networkservices-endpoints` | _Values:_  


  * `content-networkservices.googleapis.com`
  * `content-networkservices.mtls.googleapis.com`
  * `networkservices.googleapis.com`
  * `networkservices.mtls.googleapis.com`

  
global-osconfig-endpoints  |  VM Manager global API endpoints:  
`in:global-osconfig-endpoints` | _Values:_  


  * `content-osconfig.googleapis.com`
  * `content-osconfig.mtls.googleapis.com`
  * `osconfig.googleapis.com`
  * `osconfig.mtls.googleapis.com`

  
global-oslogin-endpoints  |  OS Login API endpoints:  
`in:global-oslogin-endpoints` | _Values:_  


  * `oslogin.googleapis.com`

  
global-parametermanager-endpoints  |  Parameter Manager global API Endpoints:  
`in:global-parametermanager-endpoints` | _Values:_  


  * `content-parametermanager.googleapis.com`
  * `content-parametermanager.mtls.googleapis.com`
  * `parametermanager.googleapis.com`
  * `parametermanager.mtls.googleapis.com`

  
global-policytroubleshooter-endpoints  |  Policy Troubleshooter global API endpoints:  
`in:global-policytroubleshooter-endpoints` | _Values:_  


  * `content-policytroubleshooter.googleapis.com`
  * `content-policytroubleshooter.mtls.googleapis.com`
  * `policytroubleshooter.googleapis.com`
  * `policytroubleshooter.mtls.googleapis.com`

  
global-privilegedaccessmanager-endpoints  |  Privileged Access Manager global API Endpoints:  
`in:global-privilegedaccessmanager-endpoints` | _Values:_  


  * `content-privilegedaccessmanager.googleapis.com`
  * `content-privilegedaccessmanager.mtls.googleapis.com`
  * `privilegedaccessmanager.googleapis.com`
  * `privilegedaccessmanager.mtls.googleapis.com`

  
global-progressiverollout-endpoints  |  Ripple global API endpoints:  
`in:global-progressiverollout-endpoints` | _Values:_  


  * `content-progressiverollout.googleapis.com`
  * `content-progressiverollout.mtls.googleapis.com`
  * `progressiverollout.googleapis.com`
  * `progressiverollout.mtls.googleapis.com`

  
global-pubsub-endpoints  |  Pub/Sub global API endpoints:  
`in:global-pubsub-endpoints` | _Values:_  


  * `content-pubsub.googleapis.com`
  * `content-pubsub.mtls.googleapis.com`
  * `pubsub.googleapis.com`
  * `pubsub.mtls.googleapis.com`

  
global-recommender-endpoints  |  Recommender global API Endpoints:  
`in:global-recommender-endpoints` | _Values:_  


  * `content-recommender.googleapis.com`
  * `content-recommender.mtls.googleapis.com`
  * `recommender.googleapis.com`
  * `recommender.mtls.googleapis.com`

  
global-redis-endpoints  |  Memorystore for Redis global API endpoints:  
`in:global-redis-endpoints` | _Values:_  


  * `content-redis.googleapis.com`
  * `content-redis.mtls.googleapis.com`
  * `redis.googleapis.com`
  * `redis.mtls.googleapis.com`

  
global-run-endpoints  |  Cloud Run global API endpoints:  
`in:global-run-endpoints` | _Values:_  


  * `content-run.googleapis.com`
  * `content-run.mtls.googleapis.com`
  * `run.googleapis.com`
  * `run.mtls.googleapis.com`

  
global-secretmanager-endpoints  |  Secret Manager global API endpoints:  
`in:global-secretmanager-endpoints` | _Values:_  


  * `content-secretmanager.googleapis.com`
  * `content-secretmanager.mtls.googleapis.com`
  * `secretmanager.googleapis.com`
  * `secretmanager.mtls.googleapis.com`

  
global-securesourcemanager-endpoints  |  Secure Source Manager global API Endpoints:  
`in:global-securesourcemanager-endpoints` | _Values:_  


  * `content-securesourcemanager.googleapis.com`
  * `content-securesourcemanager.mtls.googleapis.com`
  * `securesourcemanager.googleapis.com`
  * `securesourcemanager.mtls.googleapis.com`

  
global-securitycenter-endpoints  |  Cloud Security Command Center global API endpoints:  
`in:global-securitycenter-endpoints` | _Values:_  


  * `content-securitycenter.googleapis.com`
  * `content-securitycenter.mtls.googleapis.com`
  * `securitycenter.googleapis.com`
  * `securitycenter.mtls.googleapis.com`

  
global-securitycentermanagement-endpoints  |  Cloud Security Command Center Management global API endpoints:  
`in:global-securitycentermanagement-endpoints` | _Values:_  


  * `content-securitycentermanagement.googleapis.com`
  * `content-securitycentermanagement.mtls.googleapis.com`
  * `securitycentermanagement.googleapis.com`
  * `securitycentermanagement.mtls.googleapis.com`

  
global-securityposture-endpoints  |  Security Posture global API endpoints:  
`in:global-securityposture-endpoints` | _Values:_  


  * `content-securityposture.googleapis.com`
  * `content-securityposture.mtls.googleapis.com`
  * `securityposture.googleapis.com`
  * `securityposture.mtls.googleapis.com`

  
global-servicedirectory-endpoints  |  Service Directory global API endpoints:  
`in:global-servicedirectory-endpoints` | _Values:_  


  * `content-servicedirectory.googleapis.com`
  * `content-servicedirectory.mtls.googleapis.com`
  * `servicedirectory.googleapis.com`
  * `servicedirectory.mtls.googleapis.com`

  
global-servicehealth-endpoints  |  Servicehealth global API endpoints:  
`in:global-servicehealth-endpoints` | _Values:_  


  * `content-servicehealth.googleapis.com`
  * `content-servicehealth.mtls.googleapis.com`
  * `servicehealth.googleapis.com`
  * `servicehealth.mtls.googleapis.com`

  
global-servicenetworking-endpoints  |  Service Networking global API endpoints:  
`in:global-servicenetworking-endpoints` | _Values:_  


  * `content-servicenetworking.googleapis.com`
  * `content-servicenetworking.mtls.googleapis.com`
  * `servicenetworking.googleapis.com`
  * `servicenetworking.mtls.googleapis.com`

  
global-serviceusage-endpoints  |  Service Usage global API Endpoints:  
`in:global-serviceusage-endpoints` | _Values:_  


  * `content-serviceusage.googleapis.com`
  * `content-serviceusage.mtls.googleapis.com`
  * `serviceusage.googleapis.com`
  * `serviceusage.mtls.googleapis.com`

  
global-spanner-endpoints  |  Cloud Spanner global API endpoints:  
`in:global-spanner-endpoints` | _Values:_  


  * `content-spanner.googleapis.com`
  * `content-spanner.mtls.googleapis.com`
  * `spanner.googleapis.com`
  * `spanner.mtls.googleapis.com`

  
global-speech-endpoints  |  Cloud Speech global API endpoints:  
`in:global-speech-endpoints` | _Values:_  


  * `content-speech.googleapis.com`
  * `content-speech.mtls.googleapis.com`
  * `speech.googleapis.com`
  * `speech.mtls.googleapis.com`

  
global-sqladmin-endpoints  |  Cloud SQL global API endpoints:  
`in:global-sqladmin-endpoints` | _Values:_  


  * `content-sqladmin.googleapis.com`
  * `content-sqladmin.mtls.googleapis.com`
  * `sqladmin.googleapis.com`
  * `sqladmin.mtls.googleapis.com`

  
global-storagetransfer-endpoints  |  Storage Transfer Service global API Endpoints:  
`in:global-storagetransfer-endpoints` | _Values:_  


  * `content-storagetransfer.googleapis.com`
  * `content-storagetransfer.mtls.googleapis.com`
  * `storagetransfer.googleapis.com`
  * `storagetransfer.mtls.googleapis.com`

  
global-texttospeech-endpoints  |  Text-to-Speech global API Endpoints:  
`in:global-texttospeech-endpoints` | _Values:_  


  * `content-texttospeech.googleapis.com`
  * `content-texttospeech.mtls.googleapis.com`
  * `texttospeech.googleapis.com`
  * `texttospeech.mtls.googleapis.com`

  
global-tpu-endpoints  |  Cloud TPU global API endpoints:  
`in:global-tpu-endpoints` | _Values:_  


  * `content-tpu.googleapis.com`
  * `content-tpu.mtls.googleapis.com`
  * `tpu.googleapis.com`
  * `tpu.mtls.googleapis.com`

  
global-trafficdirector-endpoints  |  Traffic Director global API endpoints:  
`in:global-trafficdirector-endpoints` | _Values:_  


  * `content-trafficdirector.googleapis.com`
  * `content-trafficdirector.mtls.googleapis.com`
  * `trafficdirector.googleapis.com`
  * `trafficdirector.mtls.googleapis.com`

  
global-websecurityscanner-endpoints  |  Web Security Scanner global API endpoints:  
`in:global-websecurityscanner-endpoints` | _Values:_  


  * `content-websecurityscanner.googleapis.com`
  * `content-websecurityscanner.mtls.googleapis.com`
  * `websecurityscanner.googleapis.com`
  * `websecurityscanner.mtls.googleapis.com`

  
global-workflowexecutions-endpoints  |  Workflow Executions global API endpoints:  
`in:global-workflowexecutions-endpoints` | _Values:_  


  * `content-workflowexecutions.googleapis.com`
  * `content-workflowexecutions.mtls.googleapis.com`
  * `workflowexecutions.googleapis.com`
  * `workflowexecutions.mtls.googleapis.com`

  
global-workflows-endpoints  |  Workflows global API endpoints:  
`in:global-workflows-endpoints` | _Values:_  


  * `content-workflows.googleapis.com`
  * `content-workflows.mtls.googleapis.com`
  * `workflows.googleapis.com`
  * `workflows.mtls.googleapis.com`

  
global-workloadmanager-endpoints  |  Workload Manager global API endpoints:  
`in:global-workloadmanager-endpoints` | _Values:_  


  * `content-workloadmanager.googleapis.com`
  * `content-workloadmanager.mtls.googleapis.com`
  * `workloadmanager.googleapis.com`
  * `workloadmanager.mtls.googleapis.com`

  
global-workstations-endpoints  |  Cloud Workstations global API endpoints:  
`in:global-workstations-endpoints` | _Values:_  


  * `content-workstations.googleapis.com`
  * `content-workstations.mtls.googleapis.com`
  * `workstations.googleapis.com`
  * `workstations.mtls.googleapis.com`

  
non-eu-aiplatform-endpoints  |  Vertex AI Platform API endpoints outside of the EU:  
`in:non-eu-aiplatform-endpoints` | _Groups:_  


  * `aiplatform-africa-endpoints`
  * `aiplatform-americas-non-us-endpoints`
  * `aiplatform-asia-endpoints`
  * `aiplatform-australia-endpoints`
  * `aiplatform-europe-non-eu-endpoints`
  * `aiplatform-middleeast-endpoints`
  * `aiplatform-us-endpoints`
  * `global-aiplatform-endpoints`

  
aiplatform-africa-endpoints  |  Vertex AI Platform API endpoints in Africa:  
`in:aiplatform-africa-endpoints` | _Values:_  


  * `africa-south1-aiplatform.googleapis.com`
  * `africa-south1-aiplatform.mtls.googleapis.com`
  * `aiplatform.africa-south1.rep.googleapis.com`
  * `aiplatform.africa-south1.rep.mtls.googleapis.com`
  * `content-africa-south1-aiplatform.googleapis.com`
  * `content-africa-south1-aiplatform.mtls.googleapis.com`
  * `content-aiplatform.africa-south1.rep.googleapis.com`
  * `content-aiplatform.africa-south1.rep.mtls.googleapis.com`

  
aiplatform-americas-non-us-endpoints  |  Vertex AI Platform API endpoints in the Americas outside of the US:  
`in:aiplatform-americas-non-us-endpoints` | _Groups:_  


  * `aiplatform-canada-endpoints`
  * `aiplatform-southamerica-endpoints`

  
aiplatform-canada-endpoints  |  Vertex AI Platform API endpoints in Canada:  
`in:aiplatform-canada-endpoints` | _Values:_  


  * `aiplatform.northamerica-northeast1.rep.googleapis.com`
  * `aiplatform.northamerica-northeast1.rep.mtls.googleapis.com`
  * `aiplatform.northamerica-northeast2.rep.googleapis.com`
  * `aiplatform.northamerica-northeast2.rep.mtls.googleapis.com`
  * `content-aiplatform.northamerica-northeast1.rep.googleapis.com`
  * `content-aiplatform.northamerica-northeast1.rep.mtls.googleapis.com`
  * `content-aiplatform.northamerica-northeast2.rep.googleapis.com`
  * `content-aiplatform.northamerica-northeast2.rep.mtls.googleapis.com`
  * `content-northamerica-northeast1-aiplatform.googleapis.com`
  * `content-northamerica-northeast1-aiplatform.mtls.googleapis.com`
  * `content-northamerica-northeast2-aiplatform.googleapis.com`
  * `content-northamerica-northeast2-aiplatform.mtls.googleapis.com`
  * `northamerica-northeast1-aiplatform.googleapis.com`
  * `northamerica-northeast1-aiplatform.mtls.googleapis.com`
  * `northamerica-northeast2-aiplatform.googleapis.com`
  * `northamerica-northeast2-aiplatform.mtls.googleapis.com`

  
aiplatform-southamerica-endpoints  |  Vertex AI Platform API endpoints in South America:  
`in:aiplatform-southamerica-endpoints` | _Values:_  


  * `aiplatform.southamerica-east1.rep.googleapis.com`
  * `aiplatform.southamerica-east1.rep.mtls.googleapis.com`
  * `aiplatform.southamerica-west1.rep.googleapis.com`
  * `aiplatform.southamerica-west1.rep.mtls.googleapis.com`
  * `content-aiplatform.southamerica-east1.rep.googleapis.com`
  * `content-aiplatform.southamerica-east1.rep.mtls.googleapis.com`
  * `content-aiplatform.southamerica-west1.rep.googleapis.com`
  * `content-aiplatform.southamerica-west1.rep.mtls.googleapis.com`
  * `content-southamerica-east1-aiplatform.googleapis.com`
  * `content-southamerica-east1-aiplatform.mtls.googleapis.com`
  * `content-southamerica-west1-aiplatform.googleapis.com`
  * `content-southamerica-west1-aiplatform.mtls.googleapis.com`
  * `southamerica-east1-aiplatform.googleapis.com`
  * `southamerica-east1-aiplatform.mtls.googleapis.com`
  * `southamerica-west1-aiplatform.googleapis.com`
  * `southamerica-west1-aiplatform.mtls.googleapis.com`

  
aiplatform-asia-endpoints  |  Vertex AI Platform API endpoints in Asia Pacific:  
`in:aiplatform-asia-endpoints` | _Groups:_  


  * `aiplatform-asia-east-endpoints`
  * `aiplatform-asia-northeast-endpoints`
  * `aiplatform-asia-south-endpoints`
  * `aiplatform-asia-southeast-endpoints`

  
aiplatform-asia-east-endpoints  |  Vertex AI Platform API endpoints in East Asia (Taiwan, Hong Kong):  
`in:aiplatform-asia-east-endpoints` | _Values:_  


  * `aiplatform.asia-east1.rep.googleapis.com`
  * `aiplatform.asia-east1.rep.mtls.googleapis.com`
  * `aiplatform.asia-east2.rep.googleapis.com`
  * `aiplatform.asia-east2.rep.mtls.googleapis.com`
  * `asia-east1-aiplatform.googleapis.com`
  * `asia-east1-aiplatform.mtls.googleapis.com`
  * `asia-east2-aiplatform.googleapis.com`
  * `asia-east2-aiplatform.mtls.googleapis.com`
  * `content-aiplatform.asia-east1.rep.googleapis.com`
  * `content-aiplatform.asia-east1.rep.mtls.googleapis.com`
  * `content-aiplatform.asia-east2.rep.googleapis.com`
  * `content-aiplatform.asia-east2.rep.mtls.googleapis.com`
  * `content-asia-east1-aiplatform.googleapis.com`
  * `content-asia-east1-aiplatform.mtls.googleapis.com`
  * `content-asia-east2-aiplatform.googleapis.com`
  * `content-asia-east2-aiplatform.mtls.googleapis.com`

  
aiplatform-asia-northeast-endpoints  |  Vertex AI Platform API endpoints in Northeast Asia (Tokyo, Osaka, Seoul):  
`in:aiplatform-asia-northeast-endpoints` | _Values:_  


  * `aiplatform.asia-northeast1.rep.googleapis.com`
  * `aiplatform.asia-northeast1.rep.mtls.googleapis.com`
  * `aiplatform.asia-northeast2.rep.googleapis.com`
  * `aiplatform.asia-northeast2.rep.mtls.googleapis.com`
  * `aiplatform.asia-northeast3.rep.googleapis.com`
  * `aiplatform.asia-northeast3.rep.mtls.googleapis.com`
  * `asia-northeast1-aiplatform.googleapis.com`
  * `asia-northeast1-aiplatform.mtls.googleapis.com`
  * `asia-northeast2-aiplatform.googleapis.com`
  * `asia-northeast2-aiplatform.mtls.googleapis.com`
  * `asia-northeast3-aiplatform.googleapis.com`
  * `asia-northeast3-aiplatform.mtls.googleapis.com`
  * `content-aiplatform.asia-northeast1.rep.googleapis.com`
  * `content-aiplatform.asia-northeast1.rep.mtls.googleapis.com`
  * `content-aiplatform.asia-northeast2.rep.googleapis.com`
  * `content-aiplatform.asia-northeast2.rep.mtls.googleapis.com`
  * `content-aiplatform.asia-northeast3.rep.googleapis.com`
  * `content-aiplatform.asia-northeast3.rep.mtls.googleapis.com`
  * `content-asia-northeast1-aiplatform.googleapis.com`
  * `content-asia-northeast1-aiplatform.mtls.googleapis.com`
  * `content-asia-northeast2-aiplatform.googleapis.com`
  * `content-asia-northeast2-aiplatform.mtls.googleapis.com`
  * `content-asia-northeast3-aiplatform.googleapis.com`
  * `content-asia-northeast3-aiplatform.mtls.googleapis.com`

  
aiplatform-asia-south-endpoints  |  Vertex AI Platform API endpoints in South Asia (Mumbai, Delhi):  
`in:aiplatform-asia-south-endpoints` | _Values:_  


  * `aiplatform.asia-south1.rep.googleapis.com`
  * `aiplatform.asia-south1.rep.mtls.googleapis.com`
  * `aiplatform.asia-south2.rep.googleapis.com`
  * `aiplatform.asia-south2.rep.mtls.googleapis.com`
  * `asia-south1-aiplatform.googleapis.com`
  * `asia-south1-aiplatform.mtls.googleapis.com`
  * `asia-south2-aiplatform.googleapis.com`
  * `asia-south2-aiplatform.mtls.googleapis.com`
  * `content-aiplatform.asia-south1.rep.googleapis.com`
  * `content-aiplatform.asia-south1.rep.mtls.googleapis.com`
  * `content-aiplatform.asia-south2.rep.googleapis.com`
  * `content-aiplatform.asia-south2.rep.mtls.googleapis.com`
  * `content-asia-south1-aiplatform.googleapis.com`
  * `content-asia-south1-aiplatform.mtls.googleapis.com`
  * `content-asia-south2-aiplatform.googleapis.com`
  * `content-asia-south2-aiplatform.mtls.googleapis.com`

  
aiplatform-asia-southeast-endpoints  |  Vertex AI Platform API endpoints in Southeast Asia (Singapore, Jakarta):  
`in:aiplatform-asia-southeast-endpoints` | _Values:_  


  * `aiplatform.asia-southeast1.rep.googleapis.com`
  * `aiplatform.asia-southeast1.rep.mtls.googleapis.com`
  * `aiplatform.asia-southeast2.rep.googleapis.com`
  * `aiplatform.asia-southeast2.rep.mtls.googleapis.com`
  * `asia-southeast1-aiplatform.googleapis.com`
  * `asia-southeast1-aiplatform.mtls.googleapis.com`
  * `asia-southeast2-aiplatform.googleapis.com`
  * `asia-southeast2-aiplatform.mtls.googleapis.com`
  * `content-aiplatform.asia-southeast1.rep.googleapis.com`
  * `content-aiplatform.asia-southeast1.rep.mtls.googleapis.com`
  * `content-aiplatform.asia-southeast2.rep.googleapis.com`
  * `content-aiplatform.asia-southeast2.rep.mtls.googleapis.com`
  * `content-asia-southeast1-aiplatform.googleapis.com`
  * `content-asia-southeast1-aiplatform.mtls.googleapis.com`
  * `content-asia-southeast2-aiplatform.googleapis.com`
  * `content-asia-southeast2-aiplatform.mtls.googleapis.com`

  
aiplatform-australia-endpoints  |  Vertex AI Platform API endpoints in Australia:  
`in:aiplatform-australia-endpoints` | _Values:_  


  * `aiplatform.australia-southeast1.rep.googleapis.com`
  * `aiplatform.australia-southeast1.rep.mtls.googleapis.com`
  * `aiplatform.australia-southeast2.rep.googleapis.com`
  * `aiplatform.australia-southeast2.rep.mtls.googleapis.com`
  * `australia-southeast1-aiplatform.googleapis.com`
  * `australia-southeast1-aiplatform.mtls.googleapis.com`
  * `australia-southeast2-aiplatform.googleapis.com`
  * `australia-southeast2-aiplatform.mtls.googleapis.com`
  * `content-aiplatform.australia-southeast1.rep.googleapis.com`
  * `content-aiplatform.australia-southeast1.rep.mtls.googleapis.com`
  * `content-aiplatform.australia-southeast2.rep.googleapis.com`
  * `content-aiplatform.australia-southeast2.rep.mtls.googleapis.com`
  * `content-australia-southeast1-aiplatform.googleapis.com`
  * `content-australia-southeast1-aiplatform.mtls.googleapis.com`
  * `content-australia-southeast2-aiplatform.googleapis.com`
  * `content-australia-southeast2-aiplatform.mtls.googleapis.com`

  
aiplatform-europe-non-eu-endpoints  |  Vertex AI Platform API endpoints in Europe outside of the EU:  
`in:aiplatform-europe-non-eu-endpoints` | _Values:_  


  * `aiplatform.europe-west2.rep.googleapis.com`
  * `aiplatform.europe-west2.rep.mtls.googleapis.com`
  * `aiplatform.europe-west6.rep.googleapis.com`
  * `aiplatform.europe-west6.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west2.rep.googleapis.com`
  * `content-aiplatform.europe-west2.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west6.rep.googleapis.com`
  * `content-aiplatform.europe-west6.rep.mtls.googleapis.com`
  * `content-europe-west2-aiplatform.googleapis.com`
  * `content-europe-west2-aiplatform.mtls.googleapis.com`
  * `content-europe-west6-aiplatform.googleapis.com`
  * `content-europe-west6-aiplatform.mtls.googleapis.com`
  * `europe-west2-aiplatform.googleapis.com`
  * `europe-west2-aiplatform.mtls.googleapis.com`
  * `europe-west6-aiplatform.googleapis.com`
  * `europe-west6-aiplatform.mtls.googleapis.com`

  
aiplatform-middleeast-endpoints  |  Vertex AI Platform API endpoints in Middle East:  
`in:aiplatform-middleeast-endpoints` | _Values:_  


  * `aiplatform.me-central1.rep.googleapis.com`
  * `aiplatform.me-central1.rep.mtls.googleapis.com`
  * `aiplatform.me-central2.rep.googleapis.com`
  * `aiplatform.me-central2.rep.mtls.googleapis.com`
  * `aiplatform.me-west1.rep.googleapis.com`
  * `aiplatform.me-west1.rep.mtls.googleapis.com`
  * `content-aiplatform.me-central1.rep.googleapis.com`
  * `content-aiplatform.me-central1.rep.mtls.googleapis.com`
  * `content-aiplatform.me-central2.rep.googleapis.com`
  * `content-aiplatform.me-central2.rep.mtls.googleapis.com`
  * `content-aiplatform.me-west1.rep.googleapis.com`
  * `content-aiplatform.me-west1.rep.mtls.googleapis.com`
  * `content-me-central1-aiplatform.googleapis.com`
  * `content-me-central1-aiplatform.mtls.googleapis.com`
  * `content-me-central2-aiplatform.googleapis.com`
  * `content-me-central2-aiplatform.mtls.googleapis.com`
  * `content-me-west1-aiplatform.googleapis.com`
  * `content-me-west1-aiplatform.mtls.googleapis.com`
  * `me-central1-aiplatform.googleapis.com`
  * `me-central1-aiplatform.mtls.googleapis.com`
  * `me-central2-aiplatform.googleapis.com`
  * `me-central2-aiplatform.mtls.googleapis.com`
  * `me-west1-aiplatform.googleapis.com`
  * `me-west1-aiplatform.mtls.googleapis.com`

  
aiplatform-us-endpoints  |  Vertex AI Platform API endpoints in the United States:  
`in:aiplatform-us-endpoints` | _Groups:_  


  * `aiplatform-us-central-endpoints`
  * `aiplatform-us-east-endpoints`
  * `aiplatform-us-multi-endpoints`
  * `aiplatform-us-south-endpoints`
  * `aiplatform-us-west-a-endpoints`
  * `aiplatform-us-west-b-endpoints`

  
aiplatform-us-central-endpoints  |  Vertex AI Platform API endpoints in Central US (Iowa):  
`in:aiplatform-us-central-endpoints` | _Values:_  


  * `aiplatform.us-central1.rep.googleapis.com`
  * `aiplatform.us-central1.rep.mtls.googleapis.com`
  * `content-aiplatform.us-central1.rep.googleapis.com`
  * `content-aiplatform.us-central1.rep.mtls.googleapis.com`
  * `content-us-central1-aiplatform.googleapis.com`
  * `content-us-central1-aiplatform.mtls.googleapis.com`
  * `us-central1-aiplatform.googleapis.com`
  * `us-central1-aiplatform.mtls.googleapis.com`

  
aiplatform-us-east-endpoints  |  Vertex AI Platform API endpoints in Eastern US (South Carolina, Northern Virginia, Columbus):  
`in:aiplatform-us-east-endpoints` | _Values:_  


  * `aiplatform.us-east1.rep.googleapis.com`
  * `aiplatform.us-east1.rep.mtls.googleapis.com`
  * `aiplatform.us-east4.rep.googleapis.com`
  * `aiplatform.us-east4.rep.mtls.googleapis.com`
  * `aiplatform.us-east5.rep.googleapis.com`
  * `aiplatform.us-east5.rep.mtls.googleapis.com`
  * `content-aiplatform.us-east1.rep.googleapis.com`
  * `content-aiplatform.us-east1.rep.mtls.googleapis.com`
  * `content-aiplatform.us-east4.rep.googleapis.com`
  * `content-aiplatform.us-east4.rep.mtls.googleapis.com`
  * `content-aiplatform.us-east5.rep.googleapis.com`
  * `content-aiplatform.us-east5.rep.mtls.googleapis.com`
  * `content-us-east1-aiplatform.googleapis.com`
  * `content-us-east1-aiplatform.mtls.googleapis.com`
  * `content-us-east4-aiplatform.googleapis.com`
  * `content-us-east4-aiplatform.mtls.googleapis.com`
  * `content-us-east5-aiplatform.googleapis.com`
  * `content-us-east5-aiplatform.mtls.googleapis.com`
  * `us-east1-aiplatform.googleapis.com`
  * `us-east1-aiplatform.mtls.googleapis.com`
  * `us-east4-aiplatform.googleapis.com`
  * `us-east4-aiplatform.mtls.googleapis.com`
  * `us-east5-aiplatform.googleapis.com`
  * `us-east5-aiplatform.mtls.googleapis.com`

  
aiplatform-us-multi-endpoints  |  Vertex AI Platform API multi-region endpoints in the United States:  
`in:aiplatform-us-multi-endpoints` | _Values:_  


  * `aiplatform.us.rep.googleapis.com`
  * `aiplatform.us.rep.mtls.googleapis.com`
  * `content-aiplatform.us.rep.googleapis.com`
  * `content-aiplatform.us.rep.mtls.googleapis.com`
  * `content-us-aiplatform.googleapis.com`
  * `content-us-aiplatform.mtls.googleapis.com`
  * `us-aiplatform.googleapis.com`
  * `us-aiplatform.mtls.googleapis.com`

  
aiplatform-us-south-endpoints  |  Vertex AI Platform API endpoints in Southern US (Dallas):  
`in:aiplatform-us-south-endpoints` | _Values:_  


  * `aiplatform.us-south1.rep.googleapis.com`
  * `aiplatform.us-south1.rep.mtls.googleapis.com`
  * `content-aiplatform.us-south1.rep.googleapis.com`
  * `content-aiplatform.us-south1.rep.mtls.googleapis.com`
  * `content-us-south1-aiplatform.googleapis.com`
  * `content-us-south1-aiplatform.mtls.googleapis.com`
  * `us-south1-aiplatform.googleapis.com`
  * `us-south1-aiplatform.mtls.googleapis.com`

  
aiplatform-us-west-a-endpoints  |  Vertex AI Platform API endpoints in Western US - Set A (Oregon, Los Angeles, Salt Lake City):  
`in:aiplatform-us-west-a-endpoints` | _Values:_  


  * `aiplatform.us-west1.rep.googleapis.com`
  * `aiplatform.us-west1.rep.mtls.googleapis.com`
  * `aiplatform.us-west2.rep.googleapis.com`
  * `aiplatform.us-west2.rep.mtls.googleapis.com`
  * `aiplatform.us-west3.rep.googleapis.com`
  * `aiplatform.us-west3.rep.mtls.googleapis.com`
  * `content-aiplatform.us-west1.rep.googleapis.com`
  * `content-aiplatform.us-west1.rep.mtls.googleapis.com`
  * `content-aiplatform.us-west2.rep.googleapis.com`
  * `content-aiplatform.us-west2.rep.mtls.googleapis.com`
  * `content-aiplatform.us-west3.rep.googleapis.com`
  * `content-aiplatform.us-west3.rep.mtls.googleapis.com`
  * `content-us-west1-aiplatform.googleapis.com`
  * `content-us-west1-aiplatform.mtls.googleapis.com`
  * `content-us-west2-aiplatform.googleapis.com`
  * `content-us-west2-aiplatform.mtls.googleapis.com`
  * `content-us-west3-aiplatform.googleapis.com`
  * `content-us-west3-aiplatform.mtls.googleapis.com`
  * `us-west1-aiplatform.googleapis.com`
  * `us-west1-aiplatform.mtls.googleapis.com`
  * `us-west2-aiplatform.googleapis.com`
  * `us-west2-aiplatform.mtls.googleapis.com`
  * `us-west3-aiplatform.googleapis.com`
  * `us-west3-aiplatform.mtls.googleapis.com`

  
aiplatform-us-west-b-endpoints  |  Vertex AI Platform API endpoints in Western US - Set B (Las Vegas, Phoenix):  
`in:aiplatform-us-west-b-endpoints` | _Values:_  


  * `aiplatform.us-west4.rep.googleapis.com`
  * `aiplatform.us-west4.rep.mtls.googleapis.com`
  * `aiplatform.us-west8.rep.googleapis.com`
  * `aiplatform.us-west8.rep.mtls.googleapis.com`
  * `content-aiplatform.us-west4.rep.googleapis.com`
  * `content-aiplatform.us-west4.rep.mtls.googleapis.com`
  * `content-aiplatform.us-west8.rep.googleapis.com`
  * `content-aiplatform.us-west8.rep.mtls.googleapis.com`
  * `content-us-west4-aiplatform.googleapis.com`
  * `content-us-west4-aiplatform.mtls.googleapis.com`
  * `content-us-west8-aiplatform.googleapis.com`
  * `content-us-west8-aiplatform.mtls.googleapis.com`
  * `us-west4-aiplatform.googleapis.com`
  * `us-west4-aiplatform.mtls.googleapis.com`
  * `us-west8-aiplatform.googleapis.com`
  * `us-west8-aiplatform.mtls.googleapis.com`

  
global-aiplatform-endpoints  |  Vertex AI Platform global API endpoints:  
`in:global-aiplatform-endpoints` | _Values:_  


  * `aiplatform.googleapis.com`
  * `aiplatform.mtls.googleapis.com`
  * `content-aiplatform.googleapis.com`
  * `content-aiplatform.mtls.googleapis.com`

  
non-us-aiplatform-endpoints  |  Vertex AI Platform API endpoints outside of the US:  
`in:non-us-aiplatform-endpoints` | _Groups:_  


  * `aiplatform-africa-endpoints`
  * `aiplatform-americas-non-us-endpoints`
  * `aiplatform-asia-endpoints`
  * `aiplatform-australia-endpoints`
  * `aiplatform-eu-endpoints`
  * `aiplatform-europe-non-eu-endpoints`
  * `aiplatform-middleeast-endpoints`
  * `global-aiplatform-endpoints`

  
aiplatform-eu-endpoints  |  Vertex AI Platform API endpoints in the European Union:  
`in:aiplatform-eu-endpoints` | _Groups:_  


  * `aiplatform-eu-central-endpoints`
  * `aiplatform-eu-multi-endpoints`
  * `aiplatform-eu-north-endpoints`
  * `aiplatform-eu-southwest-endpoints`
  * `aiplatform-eu-west-a-endpoints`
  * `aiplatform-eu-west-b-endpoints`

  
aiplatform-eu-central-endpoints  |  Vertex AI Platform API endpoints in Central Europe (Warsaw):  
`in:aiplatform-eu-central-endpoints` | _Values:_  


  * `aiplatform.europe-central2.rep.googleapis.com`
  * `aiplatform.europe-central2.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-central2.rep.googleapis.com`
  * `content-aiplatform.europe-central2.rep.mtls.googleapis.com`
  * `content-europe-central2-aiplatform.googleapis.com`
  * `content-europe-central2-aiplatform.mtls.googleapis.com`
  * `europe-central2-aiplatform.googleapis.com`
  * `europe-central2-aiplatform.mtls.googleapis.com`

  
aiplatform-eu-multi-endpoints  |  Vertex AI Platform API multi-region endpoints in the European Union:  
`in:aiplatform-eu-multi-endpoints` | _Values:_  


  * `aiplatform.eu.rep.googleapis.com`
  * `aiplatform.eu.rep.mtls.googleapis.com`
  * `content-aiplatform.eu.rep.googleapis.com`
  * `content-aiplatform.eu.rep.mtls.googleapis.com`
  * `content-eu-aiplatform.googleapis.com`
  * `content-eu-aiplatform.mtls.googleapis.com`
  * `eu-aiplatform.googleapis.com`
  * `eu-aiplatform.mtls.googleapis.com`

  
aiplatform-eu-north-endpoints  |  Vertex AI Platform API endpoints in Northern Europe (Finland, Sweden):  
`in:aiplatform-eu-north-endpoints` | _Values:_  


  * `aiplatform.europe-north1.rep.googleapis.com`
  * `aiplatform.europe-north1.rep.mtls.googleapis.com`
  * `aiplatform.europe-north2.rep.googleapis.com`
  * `aiplatform.europe-north2.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-north1.rep.googleapis.com`
  * `content-aiplatform.europe-north1.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-north2.rep.googleapis.com`
  * `content-aiplatform.europe-north2.rep.mtls.googleapis.com`
  * `content-europe-north1-aiplatform.googleapis.com`
  * `content-europe-north1-aiplatform.mtls.googleapis.com`
  * `content-europe-north2-aiplatform.googleapis.com`
  * `content-europe-north2-aiplatform.mtls.googleapis.com`
  * `europe-north1-aiplatform.googleapis.com`
  * `europe-north1-aiplatform.mtls.googleapis.com`
  * `europe-north2-aiplatform.googleapis.com`
  * `europe-north2-aiplatform.mtls.googleapis.com`

  
aiplatform-eu-southwest-endpoints  |  Vertex AI Platform API endpoints in Southwest Europe (Madrid):  
`in:aiplatform-eu-southwest-endpoints` | _Values:_  


  * `aiplatform.europe-southwest1.rep.googleapis.com`
  * `aiplatform.europe-southwest1.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-southwest1.rep.googleapis.com`
  * `content-aiplatform.europe-southwest1.rep.mtls.googleapis.com`
  * `content-europe-southwest1-aiplatform.googleapis.com`
  * `content-europe-southwest1-aiplatform.mtls.googleapis.com`
  * `europe-southwest1-aiplatform.googleapis.com`
  * `europe-southwest1-aiplatform.mtls.googleapis.com`

  
aiplatform-eu-west-a-endpoints  |  Vertex AI Platform API endpoints in Western Europe - Set A (Belgium, Berlin, Turin, Frankfurt):  
`in:aiplatform-eu-west-a-endpoints` | _Values:_  


  * `aiplatform.europe-west1.rep.googleapis.com`
  * `aiplatform.europe-west1.rep.mtls.googleapis.com`
  * `aiplatform.europe-west10.rep.googleapis.com`
  * `aiplatform.europe-west10.rep.mtls.googleapis.com`
  * `aiplatform.europe-west12.rep.googleapis.com`
  * `aiplatform.europe-west12.rep.mtls.googleapis.com`
  * `aiplatform.europe-west3.rep.googleapis.com`
  * `aiplatform.europe-west3.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west1.rep.googleapis.com`
  * `content-aiplatform.europe-west1.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west10.rep.googleapis.com`
  * `content-aiplatform.europe-west10.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west12.rep.googleapis.com`
  * `content-aiplatform.europe-west12.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west3.rep.googleapis.com`
  * `content-aiplatform.europe-west3.rep.mtls.googleapis.com`
  * `content-europe-west1-aiplatform.googleapis.com`
  * `content-europe-west1-aiplatform.mtls.googleapis.com`
  * `content-europe-west10-aiplatform.googleapis.com`
  * `content-europe-west10-aiplatform.mtls.googleapis.com`
  * `content-europe-west12-aiplatform.googleapis.com`
  * `content-europe-west12-aiplatform.mtls.googleapis.com`
  * `content-europe-west3-aiplatform.googleapis.com`
  * `content-europe-west3-aiplatform.mtls.googleapis.com`
  * `europe-west1-aiplatform.googleapis.com`
  * `europe-west1-aiplatform.mtls.googleapis.com`
  * `europe-west10-aiplatform.googleapis.com`
  * `europe-west10-aiplatform.mtls.googleapis.com`
  * `europe-west12-aiplatform.googleapis.com`
  * `europe-west12-aiplatform.mtls.googleapis.com`
  * `europe-west3-aiplatform.googleapis.com`
  * `europe-west3-aiplatform.mtls.googleapis.com`

  
aiplatform-eu-west-b-endpoints  |  Vertex AI Platform API endpoints in Western Europe - Set B (Netherlands, Milan, Paris):  
`in:aiplatform-eu-west-b-endpoints` | _Values:_  


  * `aiplatform.europe-west4.rep.googleapis.com`
  * `aiplatform.europe-west4.rep.mtls.googleapis.com`
  * `aiplatform.europe-west8.rep.googleapis.com`
  * `aiplatform.europe-west8.rep.mtls.googleapis.com`
  * `aiplatform.europe-west9.rep.googleapis.com`
  * `aiplatform.europe-west9.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west4.rep.googleapis.com`
  * `content-aiplatform.europe-west4.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west8.rep.googleapis.com`
  * `content-aiplatform.europe-west8.rep.mtls.googleapis.com`
  * `content-aiplatform.europe-west9.rep.googleapis.com`
  * `content-aiplatform.europe-west9.rep.mtls.googleapis.com`
  * `content-europe-west4-aiplatform.googleapis.com`
  * `content-europe-west4-aiplatform.mtls.googleapis.com`
  * `content-europe-west8-aiplatform.googleapis.com`
  * `content-europe-west8-aiplatform.mtls.googleapis.com`
  * `content-europe-west9-aiplatform.googleapis.com`
  * `content-europe-west9-aiplatform.mtls.googleapis.com`
  * `europe-west4-aiplatform.googleapis.com`
  * `europe-west4-aiplatform.mtls.googleapis.com`
  * `europe-west8-aiplatform.googleapis.com`
  * `europe-west8-aiplatform.mtls.googleapis.com`
  * `europe-west9-aiplatform.googleapis.com`
  * `europe-west9-aiplatform.mtls.googleapis.com`

  
global-bigquery-endpoints  |  BigQuery global API endpoints:  
`in:global-bigquery-endpoints` | _Values:_  


  * `bigquery.googleapis.com`
  * `bigquery.mtls.googleapis.com`
  * `content-bigquery.googleapis.com`
  * `content-bigquery.mtls.googleapis.com`
  * `www.googleapis.com (BigQuery)`

  
global-bigqueryreservation-endpoints  |  BigQuery Reservation global API endpoints:  
`in:global-bigqueryreservation-endpoints` | _Values:_  


  * `bigqueryreservation.googleapis.com`
  * `bigqueryreservation.mtls.googleapis.com`
  * `content-bigqueryreservation.googleapis.com`
  * `content-bigqueryreservation.mtls.googleapis.com`

  
global-bigquerystorage-endpoints  |  BigQuery Storage global API endpoints:  
`in:global-bigquerystorage-endpoints` | _Values:_  


  * `bigquerystorage.googleapis.com`
  * `bigquerystorage.mtls.googleapis.com`
  * `content-bigquerystorage.googleapis.com`
  * `content-bigquerystorage.mtls.googleapis.com`

  
global-logging-endpoints  |  Cloud Logging global API endpoints:  
`in:global-logging-endpoints` | _Values:_  


  * `content-logging.googleapis.com`
  * `content-logging.mtls.googleapis.com`
  * `logging.googleapis.com`
  * `logging.mtls.googleapis.com`

  
global-storage-endpoints  |  Cloud Storage global API endpoints:  
`in:global-storage-endpoints` | _Values:_  


  * `content-storage.googleapis.com`
  * `content-storage.mtls.googleapis.com`
  * `storage.googleapis.com`
  * `storage.mtls.googleapis.com`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

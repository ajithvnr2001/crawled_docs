---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/projects.instances/reconcileNetworking/
title: Method: projects.instances.reconcileNetworking \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:44:33.130551+00:00
---

# Method: projects.instances.reconcileNetworking  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/projects.instances/reconcileNetworking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Method: projects.instances.reconcileNetworking Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * PscDnsReconcileNetworkingRequest
    * JSON representation
  * Examples
  * Try it!



Repairs and recreates networking resources for a Cloud SQL instance. For Private Service Connect (PSC), this operation recreates PSC DNS write endpoints on specified VPC networks and reconciles Private Service Connect connectivity infrastructure for the instance.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}:reconcileNetworking`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Required. Project ID of the project that contains the instance.  
`instance` |  `string` Required. Cloud SQL instance ID.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "location": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "pscDns": {
        object ([PscDnsReconcileNetworkingRequest](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/projects.instances/reconcileNetworking#PscDnsReconcileNetworkingRequest))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`location` |  `string` Optional. Region of the Cloud SQL instance.  
Specific networking reconciliation task. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`pscDns` |  `object (`[PscDnsReconcileNetworkingRequest](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/projects.instances/reconcileNetworking#PscDnsReconcileNetworkingRequest)`)` Request to recreate Private Service Connect DNS write endpoints and reconcile Private Service Connect connectivity infrastructure for the instance.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## PscDnsReconcileNetworkingRequest

Request parameters specific to PSC DNS networking reconciliation.

JSON representation  
---  
      
    
    {
      "networks": [
        string
      ],
      "force": boolean
    }  
  
Fields  
---  
`networks[]` |  `string` Optional. List of specific consumer VPC networks to reconcile. They must be specified as full resource names (e.g., "projects/my-consumer-project/global/networks/prod-vpc"). If empty, recreates Write Endpoints for all the consumer networks associated with this instance.  
`force` |  `boolean` Optional. Set `true` to force the reset and reapplication of Private Service Connect connectivity infrastructure if standard reconciliation does not resolve automated DNS issues. This operation might cause a brief disruption in network connectivity for connected VPC networks while settings are reapplied. Use this option only when standard reconciliation fails to resolve networking issues (for example, if connectivity resources are stuck in an updating or creating state).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/multi-party-compute/audit-logging/
title: Multi-party Compute audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:15:56.674352+00:00
---

# Multi-party Compute audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Multi-party Compute audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Audit Logs for Multi-party Compute API let you track administrative and data-access operations on your resources to help you monitor access and configuration changes. You can query these logs in the Logs Explorer and check which Multi-party Compute API API methods generate Cloud Audit Logs.

For more information about Cloud Audit Logs, see the following documents:

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Multi-party Compute API audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="mpc.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Multi-party Compute API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.mpc.v1alpha1.KeyRingService.GetKeyRing`  
`google.cloud.mpc.v1alpha1.KeyRingService.ListKeyRings`  
`google.cloud.mpc.v1alpha1.KeyService.GetKey`  
`google.cloud.mpc.v1alpha1.KeyService.ListKeys`  
`google.cloud.mpc.v1alpha1.ParticipantService.GetParticipant`  
`google.cloud.mpc.v1alpha1.ParticipantService.ListParticipants`  
`google.cloud.mpc.v1alpha1.PolicyEvaluationService.AuthorizePayload`  
`google.cloud.mpc.v1alpha1.PolicyManagerService.GetPolicy`  
`google.cloud.mpc.v1alpha1.PolicyManagerService.GetPolicyAuthorTrustBundle`  
`google.cloud.mpc.v1alpha1.PolicyManagerService.ListPolicies`  
`google.cloud.mpc.v1alpha1.ProposalService.FetchProposalSignature`  
`google.cloud.mpc.v1alpha1.ProposalService.GetProposal`  
`google.cloud.mpc.v1alpha1.ProposalService.ListProposals`  
`DATA_WRITE` | `google.cloud.mpc.v1alpha1.KeyRingService.CreateKeyRing`  
`google.cloud.mpc.v1alpha1.KeyRingService.DeleteKeyRing`  
`google.cloud.mpc.v1alpha1.KeyService.CreateKey`  
`google.cloud.mpc.v1alpha1.KeyService.UpdateKey`  
`google.cloud.mpc.v1alpha1.ParticipantService.CreateParticipant`  
`google.cloud.mpc.v1alpha1.PolicyManagerService.AddQuorumSignature`  
`google.cloud.mpc.v1alpha1.PolicyManagerService.CreatePolicy`  
`google.cloud.mpc.v1alpha1.PolicyManagerService.RevokePolicy`  
`google.cloud.mpc.v1alpha1.PolicyManagerService.UpdatePolicyAuthorTrustBundle`  
`google.cloud.mpc.v1alpha1.ProposalService.CreateProposal`  
`google.cloud.mpc.v1alpha1.ProposalService.RecordParticipantDecision`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Multi-party Compute API.

### `google.cloud.mpc.v1alpha1.KeyRingService`

The following audit logs are associated with methods belonging to `google.cloud.mpc.v1alpha1.KeyRingService`.

#### `CreateKeyRing`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyRingService.CreateKeyRing`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keyRings.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyRingService.CreateKeyRing" `  




#### `DeleteKeyRing`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyRingService.DeleteKeyRing`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keyRings.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyRingService.DeleteKeyRing" `  




#### `GetKeyRing`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyRingService.GetKeyRing`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keyRings.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyRingService.GetKeyRing" `  




#### `ListKeyRings`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyRingService.ListKeyRings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keyRings.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyRingService.ListKeyRings" `  




### `google.cloud.mpc.v1alpha1.KeyService`

The following audit logs are associated with methods belonging to `google.cloud.mpc.v1alpha1.KeyService`.

#### `CreateKey`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyService.CreateKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keys.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyService.CreateKey" `  




#### `GetKey`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyService.GetKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keys.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyService.GetKey" `  




#### `ListKeys`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyService.ListKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keys.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyService.ListKeys" `  




#### `UpdateKey`

  * **Method** : `google.cloud.mpc.v1alpha1.KeyService.UpdateKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/keys.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.KeyService.UpdateKey" `  




### `google.cloud.mpc.v1alpha1.ParticipantService`

The following audit logs are associated with methods belonging to `google.cloud.mpc.v1alpha1.ParticipantService`.

#### `CreateParticipant`

  * **Method** : `google.cloud.mpc.v1alpha1.ParticipantService.CreateParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/signers.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ParticipantService.CreateParticipant" `  




#### `GetParticipant`

  * **Method** : `google.cloud.mpc.v1alpha1.ParticipantService.GetParticipant`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/signers.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ParticipantService.GetParticipant" `  




#### `ListParticipants`

  * **Method** : `google.cloud.mpc.v1alpha1.ParticipantService.ListParticipants`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/signers.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ParticipantService.ListParticipants" `  




### `google.cloud.mpc.v1alpha1.PolicyEvaluationService`

The following audit logs are associated with methods belonging to `google.cloud.mpc.v1alpha1.PolicyEvaluationService`.

#### `AuthorizePayload`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyEvaluationService.AuthorizePayload`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/instances.authorizePayload - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyEvaluationService.AuthorizePayload" `  




### `google.cloud.mpc.v1alpha1.PolicyManagerService`

The following audit logs are associated with methods belonging to `google.cloud.mpc.v1alpha1.PolicyManagerService`.

#### `AddQuorumSignature`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyManagerService.AddQuorumSignature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/policies.addQuorumSignature - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyManagerService.AddQuorumSignature" `  




#### `CreatePolicy`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyManagerService.CreatePolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/policies.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyManagerService.CreatePolicy" `  




#### `GetPolicy`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyManagerService.GetPolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/policies.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyManagerService.GetPolicy" `  




#### `GetPolicyAuthorTrustBundle`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyManagerService.GetPolicyAuthorTrustBundle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/policyAuthorTrustBundles.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyManagerService.GetPolicyAuthorTrustBundle" `  




#### `ListPolicies`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyManagerService.ListPolicies`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/policies.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyManagerService.ListPolicies" `  




#### `RevokePolicy`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyManagerService.RevokePolicy`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/policies.revoke - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyManagerService.RevokePolicy" `  




#### `UpdatePolicyAuthorTrustBundle`

  * **Method** : `google.cloud.mpc.v1alpha1.PolicyManagerService.UpdatePolicyAuthorTrustBundle`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/policyAuthorTrustBundles.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.PolicyManagerService.UpdatePolicyAuthorTrustBundle" `  




### `google.cloud.mpc.v1alpha1.ProposalService`

The following audit logs are associated with methods belonging to `google.cloud.mpc.v1alpha1.ProposalService`.

#### `CreateProposal`

  * **Method** : `google.cloud.mpc.v1alpha1.ProposalService.CreateProposal`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/proposals.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ProposalService.CreateProposal" `  




#### `FetchProposalSignature`

  * **Method** : `google.cloud.mpc.v1alpha1.ProposalService.FetchProposalSignature`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/proposals.fetchProposalSignature - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ProposalService.FetchProposalSignature" `  




#### `GetProposal`

  * **Method** : `google.cloud.mpc.v1alpha1.ProposalService.GetProposal`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/proposals.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ProposalService.GetProposal" `  




#### `ListProposals`

  * **Method** : `google.cloud.mpc.v1alpha1.ProposalService.ListProposals`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/proposals.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ProposalService.ListProposals" `  




#### `RecordParticipantDecision`

  * **Method** : `google.cloud.mpc.v1alpha1.ProposalService.RecordParticipantDecision`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `mpc.googleapis.com/proposals.recordParticipantDecision - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.mpc.v1alpha1.ProposalService.RecordParticipantDecision" `  




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

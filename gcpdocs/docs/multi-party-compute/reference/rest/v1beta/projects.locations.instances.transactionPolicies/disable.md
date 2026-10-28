---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/disable/
title: Method: projects.locations.instances.transactionPolicies.disable \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:36.407820+00:00
---

# Method: projects.locations.instances.transactionPolicies.disable  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.transactionPolicies.disable Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Starts disabling a policy, or withdraws a policy that is still waiting for activation.

For an active policy, the policy stays in effect while the disable request collects the required number of Policy Author approvals through transactionPolicies.approve. Once enough approvals are recorded, the policy is disabled.

For a policy that has not yet been activated, no further approvals are needed. The policy is disabled immediately, and deactivationInfo.transition_sequence is left unset, so the policy set version does not change because the policy was never in effect. Disabled policies are kept for auditing.

Returns the following error codes:

  * NOT_FOUND: The TransactionPolicy does not exist.
  * FAILED_PRECONDITION: The policy is already disabled or already has a pending disable request.
  * INVALID_ARGUMENT: The authorization in authorizationInfo cannot be verified.
  * PERMISSION_DENIED: The caller is not an authorized Policy Author.



### HTTP request

`POST https://mpc.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*/transactionPolicies/*}:disable`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the TransactionPolicy to disable or withdraw. Format: projects/{project}/locations/{location}/instances/{instance}/transactionPolicies/{transactionPolicy} It takes the form `projects/{project}/locations/{location}/instances/{instance}/transactionPolicies/{transactionpolicies}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "authorizationInfo": {
        object ([AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo))
      }
    }  
  
Fields  
---  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Required. The Policy Author's authorization over a TransactionPolicySigningPayload with:

  * transactionPolicy: set to name
  * action: DISABLE
  * rule: set to the policy's rule

For an active policy, this authorization is recorded as the first entry in deactivationInfo.approvals. For a policy that is still waiting for activation, this single authorization is recorded in deactivationInfo.approvals and withdraws the policy immediately.  
  
### Response body

If successful, the response body contains an instance of `[TransactionPolicy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#TransactionPolicy)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/approve/
title: Method: projects.locations.instances.transactionPolicies.approve \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:38.110528+00:00
---

# Method: projects.locations.instances.transactionPolicies.approve  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/approve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.transactionPolicies.approve Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Records a Policy Author's approval for a policy that is waiting to be activated or disabled.

When this approval reaches the required number of Policy Author approvals, the server re-verifies every collected signature against the current TransactionPolicyAuthorTrustBundle before completing the transition: a policy waiting for activation becomes active, and a policy waiting to be disabled becomes disabled.

Returns the following error codes:

  * NOT_FOUND: The TransactionPolicy does not exist.
  * FAILED_PRECONDITION: The policy is not waiting for approval.
  * ALREADY_EXISTS: The Policy Author has already approved this transition.
  * INVALID_ARGUMENT: The authorization in authorizationInfo cannot be verified.
  * PERMISSION_DENIED: The caller is not an authorized Policy Author.



### HTTP request

`POST https://mpc.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*/transactionPolicies/*}:approve`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the TransactionPolicy to approve. Format: projects/{project}/locations/{location}/instances/{instance}/transactionPolicies/{transactionPolicy} It takes the form `projects/{project}/locations/{location}/instances/{instance}/transactionPolicies/{transactionpolicies}`.  
  
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
  * action: ACTIVATE when the policy is waiting for activation, or DISABLE when the policy is waiting to be disabled
  * rule: set to the policy's rule

  
  
### Response body

If successful, the response body contains an instance of `[TransactionPolicy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#TransactionPolicy)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

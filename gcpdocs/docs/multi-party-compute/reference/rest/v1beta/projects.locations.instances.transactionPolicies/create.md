---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/create/
title: Method: projects.locations.instances.transactionPolicies.create \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:38.226484+00:00
---

# Method: projects.locations.instances.transactionPolicies.create  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.transactionPolicies.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Proposes a new TransactionPolicy in an instance. The server assigns the TransactionPolicy ID.

The proposing Policy Author's authorization in authorizationInfo counts as the first approval. If only one Policy Author approval is required, the policy becomes active immediately. Otherwise, the policy waits for activation until the required number of Policy Author approvals are recorded through transactionPolicies.approve.

Returns the following error codes:

  * INVALID_ARGUMENT: The Cedar policy statement is invalid or the authorization in authorizationInfo cannot be verified.
  * ALREADY_EXISTS: The authorization in authorizationInfo was already used to create a TransactionPolicy in this instance.
  * PERMISSION_DENIED: The caller is not an authorized Policy Author.



### HTTP request

`POST https://mpc.googleapis.com/v1beta/{parent=projects/*/locations/*/instances/*}/transactionPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent instance where the TransactionPolicy will be created. Format: projects/{project}/locations/{location}/instances/{instance} It takes the form `projects/{project}/locations/{location}/instances/{instance}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transactionPolicy": {
        object ([TransactionPolicy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#TransactionPolicy))
      },
      "authorizationInfo": {
        object ([AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo))
      },
      "requestId": string
    }  
  
Fields  
---  
`transactionPolicy` |  `object (`[TransactionPolicy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#TransactionPolicy)`)` Required. The TransactionPolicy to create. Only displayName and rule are read; all other fields are ignored.  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Required. The Policy Author's authorization over a TransactionPolicySigningPayload with:

  * instance: set to parent
  * action: ACTIVATE
  * rule: set to transactionPolicy.rule

Recorded as the first entry in activationInfo.approvals.  
`requestId` |  `string` Optional. An idempotency key. Because TransactionPolicy IDs are server-generated, a client must set this to retry a create safely. If a request with the same requestId was already completed, the server returns the TransactionPolicy it created.Must be a UUID4 and not the zero UUID.  
  
### Response body

If successful, the response body contains a newly created instance of `[TransactionPolicy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#TransactionPolicy)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/recordSignerDecision/
title: Method: projects.locations.instances.keyRings.keys.transactions.recordSignerDecision \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:37.768884+00:00
---

# Method: projects.locations.instances.keyRings.keys.transactions.recordSignerDecision  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/recordSignerDecision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.keyRings.keys.transactions.recordSignerDecision Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Records a signer's decision to authorize or deny a Transaction.

Only allowed while the Transaction is `PENDING_AUTHORIZATION`. Once enough signers authorize it, the Transaction is signed. Once enough signers deny it that the thresholds can no longer be met, the Transaction moves to `REJECTED`. Each User can record at most one decision per Transaction.

The deciding User is the User whose `principal` matches the caller's authenticated identity; that User must hold a key share of the Transaction's Key.

### HTTP request

`POST https://mpc.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*/keyRings/*/keys/*/transactions/*}:recordSignerDecision`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the Transaction to record the decision for. Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}/keys/{key}/transactions/{transaction} It takes the form `projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyring}/keys/{key}/transactions/{transaction}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "decision": enum ([Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Decision)),
      "authorizationInfo": {
        object ([AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo))
      }
    }  
  
Fields  
---  
`decision` |  `enum (`[Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Decision)`)` Required. The caller's decision.  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Required. The caller's authorization over a TransactionSigningPayload, signed with the authorization key of the User whose `principal` matches the caller, with:

  * transaction: set to name
  * decision: set to decision
  * signing_input: set to the stored Transaction's signing_input

  
  
### Response body

If successful, the response body contains an instance of `[Transaction](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Transaction)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

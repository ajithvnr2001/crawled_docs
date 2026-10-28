---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/create/
title: Method: projects.locations.instances.keyRings.keys.transactions.create \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:49.356919+00:00
---

# Method: projects.locations.instances.keyRings.keys.transactions.create  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.keyRings.keys.transactions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates a new Transaction for a Key. The server assigns the Transaction ID.

The request carries the initiator's authorization, which counts as the initiator's `AUTHORIZE` decision. The initiator is the User whose `principal` matches the caller's authenticated identity; that User must have the `SIGNER` role. If the authorizations received are enough to meet the Key's thresholds, the Transaction is signed and returned in state `SIGNING_SUCCEEDED`. Otherwise it is returned in state `PENDING_AUTHORIZATION` and other signers authorize it with `transactions.recordSignerDecision`.

### HTTP request

`POST https://mpc.googleapis.com/v1beta/{parent=projects/*/locations/*/instances/*/keyRings/*/keys/*}/transactions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The Key that signs the Transaction. Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}/keys/{key} It takes the form `projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyring}/keys/{key}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transaction": {
        object ([Transaction](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Transaction))
      },
      "authorizationInfo": {
        object ([AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo))
      },
      "requestId": string
    }  
  
Fields  
---  
`transaction` |  `object (`[Transaction](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Transaction)`)` Required. The Transaction to create. Only `signing_input`, `action`, `schema`, `payload`, and `metadata` are read; output-only fields are ignored.  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Required. The initiator's authorization over a TransactionSigningPayload, signed with the authorization key of the User whose `principal` matches the caller, with:

  * key: set to parent
  * decision: AUTHORIZE
  * signing_input: set to transaction.signing_input

Recorded as the first entry in signerDecisions.  
`requestId` |  `string` Optional. An idempotency key. Because Transaction IDs are server-generated, a client must set this to retry a create safely. If a request with the same requestId was already completed, the server returns the Transaction it created instead of creating another one.Must be a UUID4 and not the zero UUID.  
  
### Response body

If successful, the response body contains a newly created instance of `[Transaction](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Transaction)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

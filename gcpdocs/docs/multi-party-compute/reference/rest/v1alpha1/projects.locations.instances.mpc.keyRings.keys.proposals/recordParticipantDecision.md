---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/recordParticipantDecision/
title: Method: projects.locations.instances.mpc.keyRings.keys.proposals.recordParticipantDecision \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:33.982035+00:00
---

# Method: projects.locations.instances.mpc.keyRings.keys.proposals.recordParticipantDecision  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/recordParticipantDecision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.mpc.keyRings.keys.proposals.recordParticipantDecision Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Submits a cryptographic signature from a key participant, recording their assent (or rejection) for the proposal.

### HTTP request

`POST https://mpc.googleapis.com/v1alpha1/{name=projects/*/locations/*/instances/*/mpc/keyRings/*/keys/*/proposals/*}:recordParticipantDecision`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The unique resource name of the proposal to record assent for. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyRing}/keys/{key}/proposals/{proposal} It takes the form `projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyring}/keys/{key}/proposals/{proposal}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "signature": string,
      "decision": enum ([Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#Decision)),
      "participant": string
    }  
  
Fields  
---  
`signature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Participant's signature over the proposal details (e.g., payload hash), created with their key share's associated private key.A base64-encoded string.  
`decision` |  `enum (`[Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#Decision)`)` Required. The decision made by the participant (e.g., APPROVED, REJECTED).  
`participant` |  `string` Required. The resource name of the participant recording their decision. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/signers/{signer}  
  
### Response body

If successful, the response body contains an instance of `[Proposal](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#Proposal)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

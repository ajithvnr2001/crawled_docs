---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals
title: REST Resource: projects.locations.instances.mpc.keyRings.keys.proposals \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:50.024616+00:00
---

# REST Resource: projects.locations.instances.mpc.keyRings.keys.proposals  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.mpc.keyRings.keys.proposals Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Proposal
    * JSON representation
  * State
  * ParticipantVote
    * JSON representation
  * Decision
  * Methods



## Resource: Proposal

Represents a cryptographic signing Proposal.

JSON representation  
---  
      
    
    {
      "name": string,
      "digest": string,
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#State)),
      "finalSignature": string,
      "createTime": string,
      "expireTime": string,
      "recordedVotes": [
        {
          object ([ParticipantVote](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#ParticipantVote))
        }
      ],
      "policyApproverSignature": string,
      "keyVersion": string,
      "requiredThreshold": integer,
      "updateTime": string,
      "initiator": string,
      "errorMessage": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique server-assigned resource name of the Proposal. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyRing}/keys/{key}/proposals/{proposal}  
`digest` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Immutable. The digest (hash) of the message to be signed. This must be provided when the proposal is created.A base64-encoded string.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#State)`)` Output only. The current state of the proposal.  
`finalSignature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The final cryptographic signature, populated only after the proposal reaches the SUCCEEDED state.A base64-encoded string.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the proposal resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the proposal is considered expired. If the proposal does not reach the READY state by this time, it may transition to FAILED. This is set by the server upon creation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`recordedVotes[]` |  `object (`[ParticipantVote](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#ParticipantVote)`)` Output only. The list of participant votes recorded for this proposal.  
`policyApproverSignature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Immutable. The signature from the Policy Approver that authorized the creation of this proposal. This is persisted for audit purposes and later propagated for multi-stage verification across task execution.A base64-encoded string.  
`keyVersion` |  `string` Required. Immutable. The resource name of the Key version used for this signing proposal. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyRing}/keys/{key}/versions/{version}  
`requiredThreshold` |  `integer` Output only. The number of assents required for this proposal to become READY. This is determined by the Key's threshold at the time of proposal creation.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the proposal resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`initiator` |  `string` Required. Immutable. The resource name of the Participant who initiated this proposal. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/signers/{signer}  
`errorMessage` |  `string` Output only. An error message detailing why the proposal failed. Populated only when the state transitions to FAILED.  
  
## State

The state of the proposal.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`PENDING_ASSENT` | The proposal has been created and authorized by a Policy Approver but has not yet received the required threshold of participant assents. The system is waiting for participants to provide their cryptographic consent via the proposals.recordParticipantDecision method.  
`IN_PROGRESS` | The signing ceremony is actively being orchestrated. This state indicates that the system has begun the Multi-party Compute.  
`SUCCEEDED` | The signing ceremony has successfully completed. The final, aggregated digital signature has been generated and is available. This is a terminal success state.  
`FAILED` | The proposal failed to complete. This can occur due to a timeout waiting for assents, an unrecoverable error during the signing ceremony, or explicit rejection by participants. This is a terminal failure state.  
  
## ParticipantVote

Metadata about a participant's vote on this proposal.

JSON representation  
---  
      
    
    {
      "participant": string,
      "voteTime": string,
      "decision": enum ([Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#Decision)),
      "signature": string,
      "signedPayload": string
    }  
  
Fields  
---  
`participant` |  `string` Output only. The resource name of the Participant who cast this vote. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/signers/{signer}  
`voteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the vote was recorded.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`decision` |  `enum (`[Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals#Decision)`)` Output only. The decision made by the participant.  
`signature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The signature provided by the participant, an attestation of their decision.A base64-encoded string.  
`signedPayload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The exact payload that was signed by the participant, used for auditing.A base64-encoded string.  
  
## Decision

The decision made by a participant regarding the proposal.

Enums  
---  
`DECISION_UNSPECIFIED` | Default value. This value is unused.  
`ASSENT` | The participant approves the proposal.  
`DISSENT` | The participant rejects the proposal.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/create)`

|  Initiates a Signing Proposal for a given Key.  
  
### `[fetchProposalSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/fetchProposalSignature)`

|  Retrieves the final assembled signature for a completed Proposal.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/get)`

|  Gets details of a single Proposal.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/list)`

|  Lists Proposals for a given Key.  
  
### `[recordParticipantDecision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys.proposals/recordParticipantDecision)`

|  Submits a cryptographic signature from a key participant, recording their assent (or rejection) for the proposal.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

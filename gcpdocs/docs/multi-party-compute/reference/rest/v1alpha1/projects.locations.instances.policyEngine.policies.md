---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies
title: REST Resource: projects.locations.instances.policyEngine.policies \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:29.200062+00:00
---

# REST Resource: projects.locations.instances.policyEngine.policies  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.policyEngine.policies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Policy
    * JSON representation
  * State
  * Rule
    * JSON representation
  * QuorumSignature
    * JSON representation
  * Methods



## Resource: Policy

Represents a single policy rule within the Quorum Policy Engine. Policies are immutable, append-only and require an M-of-N cryptographic quorum of Policy Authors for all state transitions (e.g. creation, deletion).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#State)),
      "createTime": string,
      "updateTime": string,
      "rule": {
        object ([Rule](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#Rule))
      },
      "authorId": string,
      "deleteInitiatorId": string,
      "activationSignatures": [
        {
          object ([QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature))
        }
      ],
      "createAuthorSignature": {
        object ([QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature))
      },
      "revocationSignatures": [
        {
          object ([QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature))
        }
      ],
      "globalSequence": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the policy. Format: projects/{project}/locations/{location}/instances/{instance}/policyEngine/policies/{policy}  
`displayName` |  `string` Optional. The user-provided display name for the policy.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#State)`)` Output only. The state of the policy.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the policy was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rule` |  `object (`[Rule](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#Rule)`)` Immutable. The core policy rule definition.  
`authorId` |  `string` Output only. The identifier of the Policy Author who initially created this policy draft. This policy must be signed by a quorum of Policy Authors before it becomes ACTIVE.  
`deleteInitiatorId` |  `string` Output only. The identifier of the Policy Author who initiated the deletion process. This is set when the state transitions to PENDING_DELETED.  
`activationSignatures[]` |  `object (`[QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature)`)` Output only. The M-of-N cryptographic signatures collected from Policy Authors to activate the policy.  
`createAuthorSignature` |  `object (`[QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature)`)` Required. Input only. The signature from the Policy Author requesting the initial policy creation. This field is input-only and is validated during resource creation.  
`revocationSignatures[]` |  `object (`[QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature)`)` Output only. The M-of-N cryptographic signatures collected from Policy Authors to revoke the policy.  
`globalSequence` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. A globally incrementing sequence mapped to the Spanner transaction order.  
  
## State

The current state of the policy.

Enums  
---  
`STATE_UNSPECIFIED` | State is unspecified.  
`PENDING_ACTIVE` | The policy is pending approval from the required quorum of authors to become ACTIVE.  
`ACTIVE` | The policy is active and being enforced.  
`PENDING_DELETED` | Indicates the policy is active, but an author has submitted a delete request that is awaiting M-of-N signatures.  
`DELETED` | The policy has been deleted.  
  
## Rule

Defines the actual policy logic.

JSON representation  
---  
      
    
    {
    
      // Union field engine can be only one of the following:
      "cedarDocument": string
      // End of list of possible types for union field engine.
    }  
  
Fields  
---  
Union field `engine`. Contains the policy engine rule content. `engine` can be only one of the following:  
`cedarDocument` |  `string` Optional. The policy content, written in the Cedar policy language syntax.  
  
## QuorumSignature

A quorum signature from a policy root admin.

JSON representation  
---  
      
    
    {
      "authorId": string,
      "signature": string,
      "approvalTime": string
    }  
  
Fields  
---  
`authorId` |  `string` Required. The identifier of the Policy Author providing the signature.  
`signature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The author's signature. The signature must be generated over a SHA-256 digest of: UTF8("`action:ACTION_NAME\n`") + UTF8(policy.name) + UTF8("`sequence:`") + LE_INT64(globalSequence) + serializeRuleCanonical(policy.rule)SECURITY NOTE: For initial creation or revocation proposals, the initiator signs with a placeholder globalSequence of '0' because the server assigns the real monotonic sequence number at commit time. Subsequent co-authors must sign over the actual assigned sequence number to bind their final approval to that specific version. This prevents replay attacks.Where ACTION_NAME corresponds to the target policy state: - `"ACTIVE"` for policy creation and activation signatures. - `"DELETED"` for policy revocation/deletion signatures.Where serializeRuleCanonical is defined as: - For Cedar engines: UTF8("`cedarDocument:`") + UTF8(rule.cedar_document) - For empty engines: UTF8("`engine:unset`") - If rule is missing: an empty byte slice.A base64-encoded string.  
`approvalTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The exact timestamp when the Policy Root Admin approved and generated this signature.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[addQuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/addQuorumSignature)`

|  Custom Method: Appends a software-backed author signature to a policy.  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/create)`

|  Creates a new policy in a given instance.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/get)`

|  Gets details of a single policy.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/list)`

|  Lists policies in a given instance.  
  
### `[revoke](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/revoke)`

|  Custom Method: Revokes (deletes) a policy.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

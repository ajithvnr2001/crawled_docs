---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies
title: REST Resource: projects.locations.instances.transactionPolicies \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:34.313089+00:00
---

# REST Resource: projects.locations.instances.transactionPolicies  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.transactionPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TransactionPolicy
    * JSON representation
  * Rule
    * JSON representation
  * State
  * ApprovalInfo
    * JSON representation
  * Approval
    * JSON representation
  * Methods



## Resource: TransactionPolicy

An immutable Cedar policy rule that governs whether transactions in an instance are permitted or denied before signing.

Every completed activation or disable transition receives a monotonically increasing sequence number within the instance, recorded once in activationInfo.transition_sequence or deactivationInfo.transition_sequence. This value is the policy set version produced by the transition.

Withdrawing a policy that is still waiting for activation assigns no sequence number and does not advance the policy set version.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "displayName": string,
      "rule": {
        object ([Rule](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#Rule))
      },
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#State)),
      "activationInfo": {
        object ([ApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#ApprovalInfo))
      },
      "deactivationInfo": {
        object ([ApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#ApprovalInfo))
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the TransactionPolicy. Format: projects/{project}/locations/{location}/instances/{instance}/transactionPolicies/{transactionPolicy}  
`uid` |  `string` Output only. The unique server-generated identifier of the TransactionPolicy.  
`displayName` |  `string` Optional. Immutable. User-assigned display name for the TransactionPolicy. Maximum length is 63 characters. Set at creation; TransactionPolicy resources are immutable and have no update method.  
`rule` |  `object (`[Rule](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#Rule)`)` Required. Immutable. The policy rule evaluated against transactions. To change a rule, disable this policy with transactionPolicies.disable and create a new policy with transactionPolicies.create.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#State)`)` Output only. The lifecycle state of the TransactionPolicy.  
`activationInfo` |  `object (`[ApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#ApprovalInfo)`)` Output only. The approval status and Policy Author approvals collected to activate this policy.  
`deactivationInfo` |  `object (`[ApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#ApprovalInfo)`)` Output only. The approval status and Policy Author approvals collected to disable this policy. Unset until transactionPolicies.disable is called.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the TransactionPolicy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the TransactionPolicy was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Rule

The policy rule evaluated for a TransactionPolicy.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cedarDocument": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The rule definition for this TransactionPolicy. Must be set. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cedarDocument` |  `string` Optional. A single non-empty Cedar policy statement. Must be valid Cedar syntax; invalid or empty statements are rejected with INVALID_ARGUMENT.  
End of mutually exclusive fields.  
  
## State

The lifecycle state of a TransactionPolicy.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`PENDING_ACTIVE` | The policy has been proposed and is waiting for the required number of Policy Author approvals before it becomes active. The policy is not yet enforced on transactions and can be withdrawn by calling transactionPolicies.disable.  
`ACTIVE` | The policy is active and enforced on transactions.  
`PENDING_DISABLED` | A request to disable the policy is waiting for the required number of Policy Author approvals. The policy remains in effect and is still enforced on transactions until those approvals are recorded.  
`DISABLED` | The policy is permanently disabled and is no longer enforced on new transactions, or was withdrawn before it ever became active. Disabled policies are kept for auditing.  
  
## ApprovalInfo

Tracks the Policy Author approvals for activating or disabling a TransactionPolicy.

To build an AuthorizationInfo for a policy transition, serialize a TransactionPolicySigningPayload into signedPayload and sign those bytes in signature using the private key for the Policy Author's registered User.authorization_key.

The service verifies signature over the exact signedPayload bytes as received, then unmarshals signedPayload as a TransactionPolicySigningPayload and returns INVALID_ARGUMENT if it cannot be unmarshaled or if any field does not match the transition being authorized.

JSON representation  
---  
      
    
    {
      "approvals": [
        {
          object ([Approval](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#Approval))
        }
      ],
      "transitionSequence": string,
      "requiredApprovalCount": integer
    }  
  
Fields  
---  
`approvals[]` |  `object (`[Approval](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies#Approval)`)` Output only. The Policy Author approvals collected for this transition. The first entry is the approval of the Policy Author who initiated the request. Additional entries are appended as other Policy Authors call transactionPolicies.approve.  
`transitionSequence` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The positive sequence number assigned when the required number of Policy Author approvals was reached and the transition completed. This value is the policy set version produced by this transition. Unset when either the transition is still waiting for approvals or the policy was withdrawn.  
`requiredApprovalCount` |  `integer` Output only. The number of Policy Author approvals required to complete this transition. While the transition is waiting for approvals, this reflects the instance's current threshold and may change if the threshold is updated. Once the transition completes, it is fixed to the threshold in effect when it completed.  
  
## Approval

A Policy Author's recorded approval on a policy transition.

JSON representation  
---  
      
    
    {
      "user": string,
      "authorizationInfo": {
        object ([AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo))
      },
      "approveTime": string
    }  
  
Fields  
---  
`user` |  `string` Output only. The resource name of the User who provided this approval, resolved from the caller's authenticated identity. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Output only. The cryptographic authorization provided by the Policy Author.  
`approveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the approval was recorded.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[approve](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/approve)`

|  Records a Policy Author's approval for a policy that is waiting to be activated or disabled.  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/create)`

|  Proposes a new TransactionPolicy in an instance.  
  
### `[disable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/disable)`

|  Starts disabling a policy, or withdraws a policy that is still waiting for activation.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/get)`

|  Gets details of a single TransactionPolicy, including its Cedar rule, current lifecycle state, and recorded Policy Author approvals.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.transactionPolicies/list)`

|  Lists TransactionPolicy resources in an instance, including disabled policies.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

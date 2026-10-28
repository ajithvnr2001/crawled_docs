---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users
title: REST Resource: projects.locations.instances.users \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:38.795463+00:00
---

# REST Resource: projects.locations.instances.users  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.users Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: User
    * JSON representation
  * AuthorizationKey
    * JSON representation
  * PublicKeySignatureAlgorithm
  * Role
  * State
  * RoleStatus
    * JSON representation
  * State
  * RoleApprovalInfo
    * JSON representation
  * RoleApproval
    * JSON representation
  * Methods



## Resource: User

A User is an onboarded identity within an MPC instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "principal": string,
      "authorizationKey": {
        object ([AuthorizationKey](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#AuthorizationKey))
      },
      "team": string,
      "roles": [
        enum ([Role](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#Role))
      ],
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#State)),
      "uid": string,
      "roleStatuses": [
        {
          object ([RoleStatus](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleStatus))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the User. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}  
`displayName` |  `string` Optional. User-assigned display name for the User.  
`principal` |  `string` Required. Immutable. The principal that authenticates as this User: a Google account or a BYOID (workforce identity) principal. Requests on behalf of this User must come from this principal.  
`authorizationKey` |  `object (`[AuthorizationKey](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#AuthorizationKey)`)` Optional. The public key the User signs authorizations with. Signers and policy authors need one to authorize transactions and policies.  
`team` |  `string` Optional. The resource name of the Team the User belongs to. Must be set if `roles` includes `SIGNER`, and must be empty otherwise; a request that breaks either rule fails with INVALID_ARGUMENT. Only signers hold key shares, so only signers belong to a Team. It is set when SIGNER is enabled (users.create or UserService.EnableUserRole), cleared when SIGNER is disabled, and changed with UserService.UpdateTeamAssignment. Format: projects/{project}/locations/{location}/instances/{instance}/teams/{team}  
`roles[]` |  `enum (`[Role](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#Role)`)` Optional. The roles to grant the User at creation: empty or `SIGNER` only. After that, roles change with UserService.EnableUserRole and UserService.DisableUserRole. In responses, the roles the User can use now: those that are ACTIVE or PENDING_DISABLED in `roleStatuses`. This can be empty, for example while the User's only role waits for approval.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the User was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the User was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#State)`)` Output only. The lifecycle state of the User.  
`uid` |  `string` Output only. The unique server-generated identifier of the User.  
`roleStatuses[]` |  `object (`[RoleStatus](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleStatus)`)` Output only. The status of every role the User has ever been granted. A disabled role stays here as DISABLED, so its approvals stay visible.  
  
## AuthorizationKey

The public key a user signs authorizations with. The service only ever stores the public half; the private key never leaves the user.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "algorithm": enum ([PublicKeySignatureAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#PublicKeySignatureAlgorithm))
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key material.A base64-encoded string.  
`algorithm` |  `enum (`[PublicKeySignatureAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#PublicKeySignatureAlgorithm)`)` Required. The signature algorithm of the public key.  
  
## PublicKeySignatureAlgorithm

Signature algorithms supported for user authorization keys.

Enums  
---  
`PUBLIC_KEY_SIGNATURE_ALGORITHM_UNSPECIFIED` | Not specified.  
`PUBLIC_KEY_SIGNATURE_ALGORITHM_ECDSA_SECP256K1` | ECDSA on curve secp256k1.  
`PUBLIC_KEY_SIGNATURE_ALGORITHM_EDDSA_ED25519` | EdDSA on curve Ed25519.  
  
## Role

A role that grants a User a set of capabilities.

Enums  
---  
`ROLE_UNSPECIFIED` | Not specified.  
`SIGNER` | Can hold key shares and authorize transactions.  
`POLICY_AUTHOR` | Can author and approve transaction policies.  
`ADMIN` | Can administer Users, Teams, and other instance resources.  
  
## State

The lifecycle state of a User.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`ACTIVE` | The User is enabled. Which roles the User can use is in `roleStatuses`.  
`DISABLED` | The User is disabled and cannot use any role.  
  
## RoleStatus

The status of one of a User's roles, in User.role_statuses.

Status is per role, so a change to one role doesn't affect the others. For example, a signer who is granted POLICY_AUTHOR can keep signing while POLICY_AUTHOR waits for Admin approval.

JSON representation  
---  
      
    
    {
      "role": enum ([Role](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#Role)),
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#State_1)),
      "activationInfo": {
        object ([RoleApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleApprovalInfo))
      },
      "version": string,
      "updateTime": string,
      "deactivationInfo": {
        object ([RoleApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleApprovalInfo))
      }
    }  
  
Fields  
---  
`role` |  `enum (`[Role](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#Role)`)` Output only. The role.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#State_1)`)` Output only. The lifecycle state of the role.  
`activationInfo` |  `object (`[RoleApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleApprovalInfo)`)` Output only. The Admin approvals of the role's latest ENABLE change, pending or completed. While the role is ACTIVE or PENDING_DISABLED, this is the completed quorum that authorizes the User to use it; a disable, or a disable that expires, never replaces it. Unset for SIGNER, whose changes need no Admin approval.  
`version` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The version of the role. It increases by 1 with each change that needs Admin approval, and Admins sign it in UserSigningPayload so an old approval can't be replayed. It never decreases: a change that expires or is canceled keeps its version, so its signatures can't be reused for a later change. 0 until the first such change; always 0 for SIGNER.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the role's state last changed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deactivationInfo` |  `object (`[RoleApprovalInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleApprovalInfo)`)` Output only. The Admin approvals of the role's latest DISABLE change: pending, completed or expired. Unset if the role was never disabled with Admin approval, and always for SIGNER.  
  
## State

The lifecycle state of a role.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`PENDING_ACTIVE` | The role was enabled and is waiting for Admin approval. The User cannot use it yet.  
`ACTIVE` | The User can use the role.  
`PENDING_DISABLED` | The role is being disabled and is waiting for Admin approval. The User can still use it.  
`DISABLED` | The role was disabled. The User cannot use it.  
  
## RoleApprovalInfo

The Admin approvals of one change to a User's ADMIN or POLICY_AUTHOR role.

JSON representation  
---  
      
    
    {
      "approvals": [
        {
          object ([RoleApproval](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleApproval))
        }
      ],
      "requiredApprovalCount": integer,
      "expireTime": string,
      "version": string,
      "completeTime": string
    }  
  
Fields  
---  
`approvals[]` |  `object (`[RoleApproval](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users#RoleApproval)`)` Output only. The Admin approvals collected for the change. The first entry is the approval of the Admin who requested it; others are appended as Admins call UserService.ApproveRoleChange.  
`requiredApprovalCount` |  `integer` Output only. The number of Admin approvals required to complete the change. While the change is waiting for approvals, this reflects the instance's current threshold. Once the change completes, it is fixed to the threshold in effect when it completed.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the change expires if it hasn't reached `requiredApprovalCount`. The server sets it when the change is requested. An expired change is dropped and its role returns to its previous state. Its approvals stay here for audit, with `completeTime` unset; they never replace the approvals of the other direction.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`version` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. RoleStatus.version for this change: the version the approvals signed in UserSigningPayload.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the change reached `requiredApprovalCount` and took effect. Unset while the change is pending and if it expired or was canceled.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RoleApproval

One Admin's recorded approval of a change to a User's role.

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
`user` |  `string` Output only. The resource name of the approving Admin, resolved from the caller's authenticated identity. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Output only. The Admin's signature over a UserSigningPayload that includes this role change.  
`approveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the approval was recorded.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[approveRoleChange](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/approveRoleChange)`

|  Records an Admin's approval of the User's pending role change: the roles in `PENDING_ACTIVE` or `PENDING_DISABLED` in `role_statuses`.  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/create)`

|  Creates a new User in an instance.  
  
### `[disable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/disable)`

|  Disables a User and all of their roles at once.  
  
### `[disableRole](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/disableRole)`

|  Disables one role of a User.  
  
### `[enable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/enable)`

|  Re-enables a disabled User: sets `state` back to `ACTIVE`.  
  
### `[enableRole](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/enableRole)`

|  Enables one role of a User: grants it, or re-enables it if it was disabled.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/get)`

|  Gets details of a single User.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/list)`

|  Lists Users in an instance.  
  
### `[patch](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/patch)`

|  Updates a User's `display_name`.  
  
### `[updateTeamAssignment](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.users/updateTeamAssignment)`

|  Moves a User to a different Team.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

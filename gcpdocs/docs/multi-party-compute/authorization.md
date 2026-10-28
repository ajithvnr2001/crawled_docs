---
url: https://docs.cloud.google.com/multi-party-compute/authorization/
title: Security and authorization \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:38.978682+00:00
---

# Security and authorization  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Security and authorization Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Every request to the Multi-party Compute API passes two separate checks: an Identity and Access Management check on the API method, and a check on the caller's Multi-party Compute User and its roles. This page describes both checks, the IAM permissions, and how Admins approve changes to the User roles.

## How a request is authorized

  1. **IAM check.** Before a request reaches your instance, IAM checks that the calling principal has the permission that the method requires on the resource in the request. If it doesn't, the request fails with `403 PERMISSION_DENIED` and never reaches the instance. The request is recorded in Cloud Audit Logs. For the permission that each method requires, see IAM permissions.
  2. **User and role check.** For methods that act on behalf of a User, the instance looks up the User whose `principal` matches the caller's authenticated identity, and checks that User's roles. For example, the caller of `CreateTransaction` must be a User with the `SIGNER` role. For the checks that each method makes, see User roles.



Both checks must pass. IAM roles and User roles are complementary, for example:

  * A principal that has `roles/mpc.editor` but no User with the `POLICY_AUTHOR` role can call `CreateTransactionPolicy`, but the instance rejects the request.
  * A User with the `SIGNER` role whose principal doesn't have `mpc.googleapis.com/transactions.create` can't create transactions, because IAM rejects the request first.



Approvals also carry a signature. Signers, Policy Authors, and Admins sign each approval with the authorization key registered on their User. This ensures that Policies and Transactions are untamperable and leave durable audit trails.

Participant Trusted Execution Environments (TEEs) verify these signatures before they sign a transaction or accept a transaction policy, so a request that passes both checks still can't produce a signature without valid approvals. For more information, see the [security model](https://docs.cloud.google.com/multi-party-compute/architecture#security-model).

## User roles

Each User has one of the following roles, set in `User.roles`. This role is a role in your instance, not an IAM role.

User role | What the User can do | Checked when  
---|---|---  
`SIGNER` | Holds key shares and approves transactions. Belongs to exactly one Team. | `CreateTransaction`: the caller's User must have the `SIGNER` role.  
`RecordSignerDecision`: the caller's User must hold a key share of the transaction's key.  
`ListTransactions`: if the caller's User has only the `SIGNER` role, only transactions on keys where the User holds a key share are returned.  
`POLICY_AUTHOR` | Proposes, approves, and disables transaction policies. | `CreateTransactionPolicy`, `ApproveTransactionPolicy`, `DisableTransactionPolicy`: the caller's User must be an active Policy Author with a registered authorization key.  
`ADMIN` | Manages Users, Teams, KeyRings, keys, and KeyLists. Approves changes to the `ADMIN` and `POLICY_AUTHOR` roles. | `EnableUserRole`, `DisableUserRole`, `DisableUser`, `ApproveUser` for `ADMIN` and `POLICY_AUTHOR` changes: the request must carry the calling Admin's signature. See Admin approval of role changes.  
  
The following rules apply to Users:

  * **One principal per User.** `User.principal` is set when you create the User and can't be changed. It's a Google Account or a [Workforce Identity Federation](https://docs.cloud.google.com/multi-party-compute/byoid) principal. To change a User's principal, disable the User and create a new one.
  * **One Team per Signer.** A User with the `SIGNER` role must have `Team` set. Only users with the `SIGNER` role can hold key shares, so only Signers belong to a Team. Moving a Signer to another Team uses `UpdateTeamAssignment`, which requires resharing which is planned for a later release.
  * **Authorization keys.** Signers and Policy Authors need an authorization key to sign approvals. Admins need one to request or approve changes to the `ADMIN` and `POLICY_AUTHOR` roles; managing Signers and Teams doesn't require an Admin signature.



### Status of each role

Status | Meaning | Can the User use the role?  
---|---|---  
`PENDING_ACTIVE` | The role was granted and is waiting for Admin approval. | No  
`ACTIVE` | The role is in effect. | Yes  
`PENDING_DISABLED` | The role is being removed and is waiting for Admin approval. | Yes, until the removal is approved  
`DISABLED` | The role was removed. It stays listed so its approvals remain visible. | No  
  
## Admin approval of role changes

Admins manage all User roles. Granting or removing the `ADMIN` or `POLICY_AUTHOR` role needs approval from several Admins. Granting or removing the `SIGNER` role takes effect immediately from a single Admin, without an Admin signature. The `SIGNER` role alone grants no access to keys; a Signer receives key shares only when an Admin includes the Signer or their Team in a KeyRing's key policy and creates a key.

Method | Effect on User roles  
---|---  
`CreateUser` | Each requested `ADMIN` or `POLICY_AUTHOR` role starts in `PENDING_ACTIVE`. `SIGNER` is `ACTIVE` immediately.  
`EnableUserRole` | Grants one role. `ADMIN` and `POLICY_AUTHOR` start in `PENDING_ACTIVE`; `SIGNER` is `ACTIVE` immediately.  
`DisableUserRole` | Removes one role. For `ADMIN` and `POLICY_AUTHOR`, an `ACTIVE` role becomes `PENDING_DISABLED`, and a `PENDING_ACTIVE` role is canceled immediately, without approval. `SIGNER` becomes `DISABLED` immediately.  
`DisableUser` | Removes all of the User's roles in one request, with one signature for all `ADMIN` and `POLICY_AUTHOR` changes.  
`ApproveUser` | Records one Admin's approval of the User's pending change.  
`EnableUser` | Sets a disabled User back to `ACTIVE`. It restores no roles and needs no approval.  
  
An approval works as follows:

  1. An Admin requests the change and includes `authorizationInfo`: their signature, made with their authorization key, over the role change. This request counts as the first approval.
  2. Other Admins call `ApproveUser` on the User, each with their own signature. One approval covers every pending role change of that User.
  3. When the number of approvals reaches the instance's Admin approval threshold, all of the User's pending role changes take effect together. The approvals are stored on the User in `role_statuses.approval_info`, and participant TEEs verify them.



The following rules apply to every `ADMIN` and `POLICY_AUTHOR` change:

  * **At least two active Admins.** A change that would leave the instance with fewer active Admins than the Admin approval threshold fails with `FAILED_PRECONDITION`. The instance never has fewer than two active Admins. Admins whose role is `PENDING_DISABLED` don't count as active.
  * **No self-approval.** The User being changed can't request or approve their own change. Such a request fails with `PERMISSION_DENIED`.
  * **One approval per Admin.** If an Admin approves the same change twice, the second request fails with `ALREADY_EXISTS`.
  * **One pending change per User.** While a change is pending, requests to enable a role fail with `FAILED_PRECONDITION`. Requests to disable a role are never blocked: a disable cancels pending enables, and is combined with any pending disables into one new change whose approvals start over.
  * **Expiration.** A change that doesn't reach enough approvals by `approval_info.expire_time` expires, and its roles return to their previous status.



In v1beta API, you can't disable the `SIGNER` role, or disable the User, while the User holds key shares. Replacing a Signer's key shares requires resharing, which is planned for a later release.

## IAM permissions

The following table lists each `v1beta` method, the IAM permission that it requires, and the predefined role with the fewest permissions that includes it. Each predefined role also includes every permission of the roles before it: `roles/mpc.editor` includes `roles/mpc.viewer`, and `roles/mpc.admin` includes `roles/mpc.editor`.

Resource | Method | Permission | Predefined role  
---|---|---|---  
Team | `CreateTeam` | `mpc.googleapis.com/teams.create` | `roles/mpc.admin`  
| `DeleteTeam` | `mpc.googleapis.com/teams.delete` | `roles/mpc.admin`  
| `GetTeam` | `mpc.googleapis.com/teams.get` | `roles/mpc.viewer`  
| `ListTeams` | `mpc.googleapis.com/teams.list` | `roles/mpc.viewer`  
User | `CreateUser` | `mpc.googleapis.com/users.create` | `roles/mpc.admin`  
| `UpdateUser` | `mpc.googleapis.com/users.update` | `roles/mpc.admin`  
| `EnableUserRole` | `mpc.googleapis.com/users.enableRole` | `roles/mpc.admin`  
| `DisableUserRole` | `mpc.googleapis.com/users.disableRole` | `roles/mpc.admin`  
| `ApproveUser` | `mpc.googleapis.com/users.approve` | `roles/mpc.admin`  
| `DisableUser` | `mpc.googleapis.com/users.disable` | `roles/mpc.admin`  
| `EnableUser` | `mpc.googleapis.com/users.enable` | `roles/mpc.admin`  
| `UpdateTeamAssignment` | `mpc.googleapis.com/users.updateTeamAssignment` | `roles/mpc.admin`  
| `GetUser` | `mpc.googleapis.com/users.get` | `roles/mpc.viewer`  
| `ListUsers` | `mpc.googleapis.com/users.list` | `roles/mpc.viewer`  
KeyRing | `CreateKeyRing` | `mpc.googleapis.com/keyRings.create` | `roles/mpc.admin`  
| `DeleteKeyRing` | `mpc.googleapis.com/keyRings.delete` | `roles/mpc.admin`  
| `GetKeyRing` | `mpc.googleapis.com/keyRings.get` | `roles/mpc.viewer`  
| `ListKeyRings` | `mpc.googleapis.com/keyRings.list` | `roles/mpc.viewer`  
Key | `CreateKey` | `mpc.googleapis.com/keys.create` | `roles/mpc.admin`  
| `DisableKey` | `mpc.googleapis.com/keys.update` | `roles/mpc.editor`  
| `GetKey` | `mpc.googleapis.com/keys.get` | `roles/mpc.viewer`  
| `ListKeys` | `mpc.googleapis.com/keys.list` | `roles/mpc.viewer`  
KeyList | `CreateKeyList` | `mpc.googleapis.com/keyLists.create` | `roles/mpc.admin`  
| `DeleteKeyList` | `mpc.googleapis.com/keyLists.delete` | `roles/mpc.admin`  
| `AddKeyListEntries` | `mpc.googleapis.com/keyLists.addEntries` | `roles/mpc.admin`  
| `RemoveKeyListEntries` | `mpc.googleapis.com/keyLists.removeEntries` | `roles/mpc.admin`  
| `GetKeyList` | `mpc.googleapis.com/keyLists.get` | `roles/mpc.viewer`  
| `ListKeyLists` | `mpc.googleapis.com/keyLists.list` | `roles/mpc.viewer`  
TransactionPolicy | `CreateTransactionPolicy` | `mpc.googleapis.com/transactionPolicies.create` | `roles/mpc.editor`  
| `ApproveTransactionPolicy` | `mpc.googleapis.com/transactionPolicies.approve` | `roles/mpc.editor`  
| `DisableTransactionPolicy` | `mpc.googleapis.com/transactionPolicies.disable` | `roles/mpc.editor`  
| `GetTransactionPolicy` | `mpc.googleapis.com/transactionPolicies.get` | `roles/mpc.viewer`  
| `ListTransactionPolicies` | `mpc.googleapis.com/transactionPolicies.list` | `roles/mpc.viewer`  
Transaction | `CreateTransaction` | `mpc.googleapis.com/transactions.create` | `roles/mpc.editor`  
| `RecordSignerDecision` | `mpc.googleapis.com/transactions.recordSignerDecision` | `roles/mpc.editor`  
| `GetTransaction` | `mpc.googleapis.com/transactions.get` | `roles/mpc.viewer`  
| `ListTransactions` | `mpc.googleapis.com/transactions.list` | `roles/mpc.viewer`  
  
For request and response details, see the [Multi-party Compute API REST reference](https://docs.cloud.google.com/multi-party-compute/reference/rest).

### Predefined roles

Role | Includes | Intended for  
---|---|---  
**Multi-party Compute Viewer**  
`roles/mpc.viewer` | The `roles/mpc.viewer` permissions in the preceding table: `get` and `list` on every resource. | Auditors and monitoring tools.  
**Multi-party Compute Editor**  
`roles/mpc.editor` | All `roles/mpc.viewer` permissions, plus the `roles/mpc.editor` permissions in the preceding table. | Principals of Signers and Policy Authors. Their User roles decide which of these methods the instance accepts from them.  
**Multi-party Compute Admin**  
`roles/mpc.admin` | All `roles/mpc.editor` permissions, plus the `roles/mpc.admin` permissions in the preceding table. | Principals of Admins.  
  
`v1beta` resources don't have their own IAM policies. Grant roles on the project that contains your instance, and use IAM Conditions to narrow a role to a KeyRing.

### Recommended roles for each persona

Give each person a distinct principal, a User with only the roles they need, and an IAM role that matches:

Persona | User roles | IAM role  
---|---|---  
Admin | `ADMIN` | `roles/mpc.admin`  
Policy Author | `POLICY_AUTHOR` | `roles/mpc.editor`, or a custom role with the `transactionPolicies.*` permissions  
Signer | `SIGNER` | `roles/mpc.editor`, or a custom role with the `transactions.*` permissions  
Auditor | None | `roles/mpc.viewer`  
  
Federated principals also need the Service Usage Consumer role (`roles/serviceusage.serviceUsageConsumer`) on the consumer project. For more information, see [Configure Workforce Identity Federation (BYOID)](https://docs.cloud.google.com/multi-party-compute/byoid).

## Custom roles

To give a principal only the permissions it needs, create a [custom IAM role](https://docs.cloud.google.com/iam/docs/creating-custom-roles). For example, the following role lets a Signer view transactions and approve or deny them, but not create them:
    
    
    gcloud iam roles create mpcTransactionApprover \
      --project=PROJECT_ID \
      --title="MPC transaction approver" \
      --description="View MPC transactions and record signer decisions" \
      --permissions="mpc.googleapis.com/transactions.get,mpc.googleapis.com/transactions.list,mpc.googleapis.com/transactions.recordSignerDecision"
    

Replace `PROJECT_ID` with the ID of the project that contains your instance.

The instance still checks the caller's User: the User must hold a key share of the transaction's key to record a decision.

## IAM Conditions

You can narrow a role binding to the resources in one KeyRing with an [IAM condition](https://docs.cloud.google.com/iam/docs/conditions-overview) on the resource name. For example, if two business units share an instance and each has its own KeyRing, you can grant each unit's Signers `roles/mpc.editor` only on their own KeyRing:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
      --role="roles/mpc.editor" \
      --condition="expression=resource.name.startsWith('projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/keyRings/KEYRING_ID'),title=keyring-scoped-editor"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains your instance.
  * `SA_NAME`: the name of the service account.
  * `LOCATION`: the region of your instance.
  * `INSTANCE_ID`: the ID of your instance.
  * `KEYRING_ID`: the ID of the KeyRing.



`v1beta` resource names don't contain `/mpc/`. A condition copied from the Private Preview (`v1alpha1`) documentation, such as `.../instances/INSTANCE_ID/mpc/keyRings/KEYRING_ID`, doesn't match any `v1beta` resource.

Users, Teams, KeyLists, and transaction policies belong to the instance, not to a KeyRing, so a KeyRing-scoped binding doesn't grant access to them.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/multi-party-compute/policy-evaluation/
title: Transaction policy evaluation \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:40.581175+00:00
---

# Transaction policy evaluation  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/policy-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Transaction policy evaluation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Before Multi-party Compute signs a transaction, it evaluates the transaction against the transaction policies in your instance. This document describes which policies are evaluated, how a policy moves through its lifecycle, what a policy can check, and why a transaction is denied.

## How a transaction is evaluated

A transaction policy is a single [Cedar](https://docs.cedarpolicy.com/) `permit` or `forbid` statement. When a Signer calls `CreateTransaction`, the instance decodes the unsigned transaction in `Transaction.payload` with the parser for `Transaction.schema`, and evaluates every enforced policy against the transaction before any key share is used. A policy is enforced when its state is `ACTIVE` or `PENDING_DISABLED`. For more information, see Policy lifecycle.

The decision follows three rules:

  1. **Deny by default.** A transaction is permitted only if at least one `permit` policy matches it. With no enforced policies, every transaction is denied.
  2. **Forbid wins.** If any `forbid` policy matches, the transaction is denied, even if `permit` policies also match.
  3. **A policy that fails to evaluate doesn't match.** For example, a policy that reads an optional context attribute that the transaction doesn't have fails to evaluate. The instance records the error, skips that policy, and decides with the remaining enforced policies. This applies to `forbid` policies too, so write `forbid` policies that can't fail on a missing attribute. For an example, see Scenario 8 and Scenario 9.



A transaction that contains several transfers, such as a Solana transaction with several transfer instructions, is evaluated once for each transfer. The transaction is permitted only if every transfer is permitted. If any transfer is denied or can't be decoded, the whole transaction is denied.

Each evaluation, permit or deny, produces an evaluation record that is returned on the transaction in `Transaction.policyEvaluationRecord`.

The decision controls whether the instance can sign the transaction without waiting for more signers:

  * **`PERMIT`** : if the `CreateTransaction` request already carries enough signer authorizations to meet the KeyRing's key policy, the transaction moves to `SIGNING` right away. Otherwise it's created in `PENDING_AUTHORIZATION` and waits for more signers.
  * **`DENY`** : the instance doesn't sign the transaction automatically. The transaction is created in `PENDING_AUTHORIZATION` with `policyEvaluationRecord.decision` set to `DENY`. Signers can review the evaluation record and deny the transaction (`RecordSignerDecision` with `DENY`) or authorize it anyway (`AUTHORIZE`). The transaction is signed only if enough signers authorize it to meet the key policy.



A transaction policy is a guardrail on automatic signing, not a block on signers: signers can authorize a transaction that the policies deny. The original `PolicyEvaluationRecord` stays attached to the transaction for auditing.

## Policy lifecycle

Transaction policies can't be changed. `TransactionPolicy` has no update method, and its `rule` is immutable. To change a rule, disable the policy with `DisableTransactionPolicy` and create a new policy with `CreateTransactionPolicy`.

Activating or disabling a policy needs approvals from a quorum of Policy Authors (Users with an active `POLICY_AUTHOR` role in `User.roleStatuses`). Each Policy Author signs a `TransactionPolicySigningPayload` that names the policy (or, for `CreateTransactionPolicy`, the instance), the action (`ACTIVATE` or `DISABLE`), and `rule.cedarDocument`. The request that proposes a change counts as the first approval. Other Policy Authors approve with `ApproveTransactionPolicy`. The number of approvals needed is in `activationInfo.requiredApprovals` and `deactivationInfo.requiredApprovals`. If the instance needs only one approval, the change takes effect immediately.

The following table describes each policy state and whether policies in that state are enforced:

State | Meaning | Enforced?  
---|---|---  
`PENDING_ACTIVE` | The policy was proposed and is waiting for Policy Author approvals. | No  
`ACTIVE` | The policy has `activationInfo.requiredApprovals` approvals. | Yes  
`PENDING_DISABLED` | A Policy Author asked to disable the policy, and the request is waiting for approvals. | Yes, until the request has `deactivationInfo.requiredApprovals` approvals  
`DISABLED` | The policy was disabled, or was withdrawn before it became active. Disabled policies are kept for auditing. | No  
  
A policy moves through these states in one direction:

  * `PENDING_ACTIVE` to `ACTIVE`: the activation has enough approvals.
  * `PENDING_ACTIVE` to `DISABLED`: a Policy Author withdraws the policy with `DisableTransactionPolicy` before it becomes active.
  * `ACTIVE` to `PENDING_DISABLED`: a Policy Author calls `DisableTransactionPolicy`.
  * `PENDING_DISABLED` to `DISABLED`: the disable request has enough approvals.



A policy enters each pending state at most once. A disabled policy can't be enabled again; create a new policy instead.

For who can call these methods, see [User roles](https://docs.cloud.google.com/multi-party-compute/authorization#user-roles).

### Policy set version

The _policy set_ is the set of policies that are enforced (`ACTIVE` or `PENDING_DISABLED`) at a point in time. Each time an activation or a disable completes, the instance gives that transition the next number in a counter for the instance, and records it in `activationInfo.transitionSequence` or `deactivationInfo.transitionSequence`. That number is the _policy set version_ produced by the transition.

The following table shows how the policy set version changes over a sequence of events:

Event | Transition sequence | Enforced policies  
---|---|---  
Policy A is activated. | A: `activationInfo.transitionSequence` = 1 | A  
Policy B is activated. | B: `activationInfo.transitionSequence` = 2 | A, B  
Policy C is proposed (`PENDING_ACTIVE`), then withdrawn. | None | A, B  
A disable request for policy A is approved. | A: `deactivationInfo.transitionSequence` = 3 | B  
  
Withdrawing a `PENDING_ACTIVE` policy never changes the set of enforced policies, so it gets no transition sequence and doesn't change the policy set version. While a transition is waiting for approvals, its `transitionSequence` is unset.

Each evaluation reads the policies, KeyLists, and keys as of the transaction's `createTime`, and records the highest completed transition sequence at that time in `policyEvaluationRecord.policySetVersion`. If two evaluations have the same policy set version, they used the same policies.

## The Cedar request

A Cedar request has a principal, an action, a resource, and a context. For example:
    
    
    permit (
      principal == User::"alice@example.com",
      action == Action::"buy_transaction",
      resource == Resource::"transaction_management"
    )
    when {
      context.principal_keyring == "institutional-treasury" &&
      context has fiat_amount && context.fiat_amount <= 10000
    };
    

### How a User maps to the Cedar principal

The principal is the transaction's initiator: the User whose `principal` matches the authenticated identity of the caller of `CreateTransaction`. That User must have an active `SIGNER` role. In Cedar, the principal is a `User` entity whose ID is the User's `principal` field, for example `User::"alice@example.com"`.

The instance doesn't pass any entity data to Cedar. A `User` entity has no attributes and no parents, so:

  * `principal == User::"alice@example.com"` matches transactions that Alice initiates.
  * `principal in Team::"treasury"` never matches. To limit who can sign with a key, use the KeyRing's [key policy](https://docs.cloud.google.com/multi-party-compute/overview#key-policies). To scope a rule to a group of keys, check `context.principal_keyring`.
  * A rule that reads an attribute of `principal`, such as `principal.team`, fails to evaluate.



A User's `principal` can't be changed, so a rule that names a principal keeps referring to the same identity.

### Action and resource

  * **`action`** : the value of `Transaction.action` in the `CreateTransaction` request, formatted as a Cedar `Action` entity. `CreateTransaction` accepts the following actions:

Action | Used for  
---|---  
`Action::"buy_transaction"` | A transaction that acquires an asset.  
`Action::"sell_transaction"` | A transaction that disposes of an asset.  
`Action::"internal_transfer_transaction"` | A transfer of an asset, such as a payment or a sweep between keys.  
  
The initiator chooses the action; Multi-party Compute doesn't infer it from the payload. A rule can match one action (`action == Action::"buy_transaction"`), a list of actions (`action in [Action::"buy_transaction", Action::"sell_transaction"]`), or leave `action` unconstrained to match every action.

  * **`resource`** : always `Resource::"transaction_management"` for transaction evaluations. A rule can check `resource == Resource::"transaction_management"` or leave `resource` unconstrained.




## Context attributes

The context holds the attributes that policies check. They come from two places:

  * **The transaction payload and the signing key.** The instance decodes `Transaction.payload` and adds the IDs of the signing key and its KeyRing. These attributes are `principal_keyring`, `principal_key`, `blockchain`, `schema`, `secondary_key`, `amount_token_scaled`, `token_symbol`, `contract_address`, `chain_id`, `max_fee_atomic`, `payload`, and `time_stamp`. For the full table and the behavior for each blockchain, see [Write transaction policy rules](https://docs.cloud.google.com/multi-party-compute/writing-rules).
  * **The transaction's`metadata` field,** which the initiator sets in `CreateTransaction`.



The following table describes the metadata attributes:

`Transaction.metadata` field | Cedar attribute | Cedar type | Value  
---|---|---|---  
`fiatAmount` | `context.fiat_amount` | `Long` | The value of the transaction in whole US dollars (`google.type.Money`). `currencyCode` must be `USD`, `units` must be zero or more, and `nanos` must be `0`.  
`validity` | `context.validity` | `Long` | How long the transaction is valid (`google.protobuf.Duration`), in whole seconds. Must be more than 0 seconds, with no fractional seconds.  
`principalValue1` | `context.principal_value1` | `String` | Any value that you define, up to 256 characters, for example a trading desk or cost center.  
`principalValue2` | `context.principal_value2` | `String` | Any value that you define, up to 256 characters, for example an internal ticket or counterparty ID.  
  
The following rules apply to metadata:

  * **Unset fields aren't in the context.** If a transaction has no `fiatAmount`, `context.fiat_amount` doesn't exist, and a policy that reads it fails to evaluate. Check for the attribute with `has` first, as in `context has fiat_amount && context.fiat_amount <= 10000`.
  * **Invalid metadata fails the request.** If a field breaks the rules in the preceding table, for example a `fiatAmount` in `EUR` or with non-zero `nanos`, a `validity` of 0 seconds, or a `principalValue1` longer than 256 characters, `CreateTransaction` fails with `INVALID_ARGUMENT` and no policy is evaluated.
  * **The instance doesn't check metadata against the transaction.** `fiatAmount` is what the initiator says the transaction is worth. Other signers see the metadata in `Transaction.metadata` and `policyEvaluationRecord.evaluationContext` before they authorize it. To limit on-chain amounts independently of the metadata, check `context.amount_token_scaled` and `context.contract_address`.
  * **Metadata can't be changed** after the transaction is created.



### KeyRings

A [KeyRing](https://docs.cloud.google.com/multi-party-compute/overview#key-policies) groups keys. Every transaction's context has `principal_keyring` and `principal_key`, so a rule can apply to every key in a KeyRing, including keys created later, and a KeyRing can be an entry in a KeyList. For more information and an example rule, see [KeyRings](https://docs.cloud.google.com/multi-party-compute/writing-rules#keyrings).

### KeyLists

A [KeyList](https://docs.cloud.google.com/multi-party-compute/overview#keylists) is a named list of blockchain addresses that policies can refer to, for example as an allowlist of destinations. Each entry is one of the following:

  * A manual entry (`manualEntry`): an address that the instance doesn't manage, with optional `source` and `reason` fields.
  * A key in the instance (`key`): matches the key's addresses.
  * A KeyRing in the instance (`keyRing`): matches the addresses of every active key in the KeyRing, including keys created after the entry was added.



KeyLists can change after a policy is approved. When you add or remove an entry with `AddKeyListEntries` or `RemoveKeyListEntries`, every policy that refers to the KeyList uses the new entries from the next evaluation, without new Policy Author approvals. A KeyList can't be deleted with `DeleteKeyList` while a `PENDING_ACTIVE`, `ACTIVE`, or `PENDING_DISABLED` policy refers to it.

#### KeyLists in the Cedar context

At evaluation time, the instance expands each KeyList into a flat `Set` of `String` blockchain addresses: the manual entries, plus the addresses derived from every key and KeyRing entry. Each set is passed to Cedar as `context.key_lists["<var>KEY_LIST_ID</var>"]`, where KEY_LIST_ID is the `{keyList}` ID in the KeyList's resource name, for example `trusted-destinations` for `projects/my-project/locations/us-central1/instances/my-instance/keyLists/trusted-destinations`.

A rule tests membership with the Cedar `contains` operator against the decoded destination address, `context.secondary_key`. For example, to permit transfers only to addresses in the `trusted-destinations` KeyList:
    
    
    // Assuming you created a KeyList with ID "trusted-destinations":
    permit (principal, action, resource)
    when { context.key_lists["trusted-destinations"].contains(context.secondary_key) };
    

To deny transfers to any address in the `blocked-addresses` KeyList:
    
    
    // Assuming you created a KeyList with ID "blocked-addresses":
    forbid (principal, action, resource)
    when { context.key_lists["blocked-addresses"].contains(context.secondary_key) };
    

Keep the following in mind:

  * **Use bracket syntax, not dot syntax, for the KeyList ID.** Cedar's dot syntax (`context.key_lists.trusted-destinations`) fails to parse when the ID contains a hyphen, which Cedar reads as subtraction, or starts with a digit, as a server-generated UUID can. Bracket syntax, `context.key_lists["<var>KEY_LIST_ID</var>"]`, works for every ID.
  * `key_lists` is always present, and a rule can read a KeyList in it directly. `CreateTransactionPolicy` verifies that every KeyList that the rule refers to exists, and `DeleteKeyList` refuses to delete a KeyList while a policy refers to it. Use `context.key_lists has "<var>KEY_LIST_ID</var>"` only when a rule refers to a KeyList that might not exist yet.
  * Addresses are compared as strings. `secondary_key` uses the format that [Write transaction policy rules](https://docs.cloud.google.com/multi-party-compute/writing-rules) describes for each blockchain, for example mixed-case EIP-55 checksum format for Ethereum. Add manual entries in the same format.
  * A Solana token transfer's `secondary_key` is the destination token account, not the owner's wallet. To allow a wallet, add its token account for each mint that you allow.



Each evaluation resolves KeyList membership as of the transaction's `createTime`, the same time as the policies, and records the result in `policyEvaluationRecord.keyListMemberships`: the KeyList, the address tested, whether it was a member, and the entry that matched.

Because a KeyList changes what a policy permits, limit who can change it. KeyList methods need `roles/mpc.admin`. For more information, see [IAM permissions](https://docs.cloud.google.com/multi-party-compute/authorization#permissions).

## Deny reasons

When `policyEvaluationRecord.decision` is `DENY`, `policyEvaluationRecord.denyReason` says why. The following table describes each deny reason:

Deny reason | When | Determining policies  
---|---|---  
`FORBID_RULE_MATCHED` | At least one enforced `forbid` policy matched. | The `forbid` policies that matched.  
`NO_PERMIT_RULE_MATCHED` | The payload decoded, no `forbid` policy matched, no policy failed to evaluate, and no `permit` policy matched. | None  
`EVALUATION_ERROR` | No `permit` or `forbid` policy matched, and at least one policy failed to evaluate, for example because it reads an optional attribute that isn't in the context. | None. `evaluationErrors` lists the errors.  
`UNRECOGNIZED_PAYLOAD` | The instance couldn't decode `Transaction.payload` or project it into a context, for example because of malformed bytes, an unsupported instruction or contract operation, or a Bitcoin transaction with several recipients. No policy is evaluated. | None. `evaluationErrors` lists the parser error.  
  
The reasons are decided in the following order:

  1. If the payload can't be decoded or projected into a context, the decision is `DENY` with `UNRECOGNIZED_PAYLOAD`.
  2. Otherwise, every enforced policy is evaluated. If any `forbid` policy matches, the decision is `DENY` with `FORBID_RULE_MATCHED`, even if `permit` policies also matched or other policies failed to evaluate.
  3. Otherwise, if at least one `permit` policy matches, the decision is `PERMIT`. Errors from other policies are still recorded in `evaluationErrors`.
  4. Otherwise, the decision is `DENY` with `EVALUATION_ERROR` if any policy failed to evaluate, or `NO_PERMIT_RULE_MATCHED` if every policy evaluated without matching.



Errors are recorded even when the decision is `PERMIT`, so check the evaluation record for policies that never match because they always fail.

## Scenarios

In Scenarios 1 to 9, Alice (`User::"alice@example.com"`) creates a valid Ethereum transfer with `action` set to `Action::"internal_transfer_transaction"` and this metadata, unless the scenario says otherwise:
    
    
    "metadata": {
      "fiatAmount": {"currencyCode": "USD", "units": "5000"},
      "principalValue1": "treasury-desk"
    }
    

The transaction has no `validity` and no `principalValue2`.

The following table summarizes each scenario:

Scenario | Enforced policies or payload | Decision | Deny reason  
---|---|---|---  
1 | None | `DENY` | `NO_PERMIT_RULE_MATCHED`  
2 | One `permit` that matches | `PERMIT` |   
3 | One `permit` that doesn't match | `DENY` | `NO_PERMIT_RULE_MATCHED`  
4 | Two `permit`, one matches | `PERMIT` |   
5 | A `permit` and a `forbid` that both match | `DENY` | `FORBID_RULE_MATCHED`  
6 | A `permit` that reads a missing attribute | `DENY` | `EVALUATION_ERROR`  
7 | The same `permit`, with `has` | `DENY` | `NO_PERMIT_RULE_MATCHED`  
8 | A `forbid` that reads a missing attribute, and a `permit` that matches | `PERMIT` |   
9 | A `forbid` that requires an attribute | `DENY` | `FORBID_RULE_MATCHED`  
10 | A payload that can't be decoded | `DENY` | `UNRECOGNIZED_PAYLOAD`  
  
### Scenario 1: No enforced policies

The instance has no `ACTIVE` or `PENDING_DISABLED` policies.

**Decision** : `DENY`, `NO_PERMIT_RULE_MATCHED`. Without a matching `permit` policy, every transaction is denied. In a new instance, no transaction is signed automatically until Policy Authors activate a `permit` policy; signers must authorize each one.

### Scenario 2: One permit that matches
    
    
    permit (principal, action, resource)
    when { context has fiat_amount && context.fiat_amount <= 10000 };
    

**Decision** : `PERMIT`. The amount, 5,000, is at most 10,000. `determiningPolicyIds` lists this policy.

### Scenario 3: One permit that doesn't match
    
    
    permit (principal, action, resource)
    when { context has fiat_amount && context.fiat_amount <= 1000 };
    

**Decision** : `DENY`, `NO_PERMIT_RULE_MATCHED`. The amount, 5,000, is more than 1,000, and no other policy permits the transaction.

### Scenario 4: Two permits, one matches

Policy A:
    
    
    permit (principal, action, resource)
    when { context has fiat_amount && context.fiat_amount <= 1000 };
    

Policy B:
    
    
    permit (
      principal == User::"alice@example.com",
      action == Action::"internal_transfer_transaction",
      resource == Resource::"transaction_management"
    )
    when {
      context has fiat_amount && context.fiat_amount <= 25000 &&
      context has principal_value1 && context.principal_value1 == "treasury-desk"
    };
    

**Decision** : `PERMIT`. Policy A doesn't match, but Policy B does. One matching `permit` policy is enough. `determiningPolicyIds` lists only Policy B.

### Scenario 5: A forbid overrides a permit

Policy A:
    
    
    permit (principal, action, resource)
    when { context has fiat_amount && context.fiat_amount <= 10000 };
    

Policy B:
    
    
    forbid (principal, action, resource)
    when { context has principal_value1 && context.principal_value1 == "treasury-desk" };
    

**Decision** : `DENY`, `FORBID_RULE_MATCHED`. Both policies match, and `forbid` wins. `determiningPolicyIds` lists only Policy B.

### Scenario 6: A permit reads a missing attribute
    
    
    permit (principal, action, resource)
    when { context.validity <= 3600 };
    

**Decision** : `DENY`, `EVALUATION_ERROR`. The transaction has no `validity`, so `context.validity` doesn't exist and the policy fails to evaluate. No other policy permits the transaction. `evaluationErrors` lists the error.

### Scenario 7: The same permit, with has
    
    
    permit (principal, action, resource)
    when { context has validity && context.validity <= 3600 };
    

**Decision** : `DENY`, `NO_PERMIT_RULE_MATCHED`. `context has validity` is false, so the policy evaluates to false instead of failing. The transaction is still denied, but the reason shows that the policy evaluated and didn't match.

### Scenario 8: A forbid reads a missing attribute

Policy A:
    
    
    permit (principal, action, resource)
    when { context has fiat_amount && context.fiat_amount <= 10000 };
    

Policy B:
    
    
    forbid (principal, action, resource)
    when { context.principal_value2 == "sanctioned-counterparty" };
    

**Decision** : `PERMIT`. The transaction has no `principalValue2`, so Policy B fails to evaluate and is skipped. Policy A matches. `determiningPolicyIds` lists Policy A, and `evaluationErrors` lists the error from Policy B.

**Caution:** A `forbid` policy that fails to evaluate doesn't deny the transaction. An initiator can leave out a metadata field to skip a `forbid` policy that reads it. To deny transactions that don't have the attribute, use `has` or `unless` as shown in Scenario 9.

### Scenario 9: A forbid that requires an attribute

Policy A is the `permit` policy from Scenario 8. Policy B:
    
    
    forbid (principal, action, resource)
    unless { context has fiat_amount };
    

**Decision** : `PERMIT` for the transaction in these scenarios, which has a `fiatAmount`. If Alice leaves out `fiatAmount`, the decision is `DENY`, `FORBID_RULE_MATCHED`: `context has fiat_amount` is false, so the `forbid` policy matches. This policy can't fail to evaluate, because it only uses `has`.

To combine a required attribute with a check on its value in one `forbid` policy, check for the attribute first:
    
    
    forbid (principal, action, resource)
    unless { context has fiat_amount && context.fiat_amount <= 10000 };
    

### Scenario 10: A payload that can't be decoded

Alice creates a transaction whose `payload` can't be decoded by the parser for `Transaction.schema`, for example truncated RLP bytes, a Bitcoin PSBT with several recipients, or a Solana transaction with an unsupported instruction.

**Decision** : `DENY`, `UNRECOGNIZED_PAYLOAD`. No policy is evaluated. `evaluationErrors` lists the parser error, and `determiningPolicyIds` is empty.

## Evaluation record

Each evaluation produces a `PolicyEvaluationRecord` that can't be changed. It is returned in `Transaction.policyEvaluationRecord` and has the following fields:

Field | Value  
---|---  
`decision` | `PERMIT` or `DENY`.  
`denyReason` | One of the deny reasons. Unset when the decision is `PERMIT`.  
`determiningPolicyIds` | On `PERMIT`, the IDs of the `permit` policies that matched. On `FORBID_RULE_MATCHED`, the IDs of the `forbid` policies that matched. Otherwise empty.  
`evaluationErrors` | The errors from policies that failed to evaluate, or the parser error when `denyReason` is `UNRECOGNIZED_PAYLOAD`.  
`evaluationContext` | The Cedar context that the policies were evaluated against, as a `google.protobuf.Struct`. 64-bit integers are stored as decimal strings to keep their precision.  
`policySetVersion` | The policy set version that the evaluation used.  
`keyListMemberships` | The KeyList memberships resolved during the evaluation.  
`intentDigest` | The lowercase hex-encoded digest of the transaction payload that was evaluated. The hash depends on the payload's schema: Keccak-256 of the transaction for `ETHEREUM_TX_V2`, the sighash of the first input for `BITCOIN_TX_V2`, SHA-256 of the unsigned message for `SOLANA_TX_V1`, and the EIP-712 signing digest, `keccak256(0x1901 ++ domainSeparator ++ hashStruct(message))`, for `EIP712_TYPED_DATA_V1`.  
`evaluationTime` | When the evaluation ran.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

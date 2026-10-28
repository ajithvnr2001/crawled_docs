---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions
title: REST Resource: projects.locations.instances.keyRings.keys.transactions \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:47.326496+00:00
---

# REST Resource: projects.locations.instances.keyRings.keys.transactions  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.keyRings.keys.transactions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Transaction
    * JSON representation
  * State
  * SignerDecision
    * JSON representation
  * Decision
  * TransactionMetadata
    * JSON representation
  * Money
    * JSON representation
  * PayloadSchema
  * PolicyEvaluationRecord
    * JSON representation
  * Decision
  * DenyReason
  * KeyListMembership
    * JSON representation
  * Methods



## Resource: Transaction

A Transaction is a request to sign a payload with a Key. It records each signer's decision and, once signed, the final signature.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#State)),
      "finalSignature": string,
      "signerDecisions": [
        {
          object ([SignerDecision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#SignerDecision))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "uid": string,
      "expireTime": string,
      "stateMessage": string,
      "metadata": {
        object ([TransactionMetadata](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#TransactionMetadata))
      },
      "action": string,
      "schema": enum ([PayloadSchema](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#PayloadSchema)),
      "payload": string,
      "policyEvaluationRecord": {
        object ([PolicyEvaluationRecord](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#PolicyEvaluationRecord))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "digest": string,
      "rawMessage": string
      // End of mutually exclusive fields.
      "recoveryId": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Transaction. Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}/keys/{key}/transactions/{transaction}  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#State)`)` Output only. The lifecycle state of the Transaction.  
`finalSignature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The signature produced by the Key. Set once the Transaction is `SIGNING_SUCCEEDED`. The encoding depends on the Key's algorithm:

  * `EC_SIGN_SECP256K1`: 64 bytes, `r || s`, each a 32-byte big-endian integer. `s` is normalized to the lower half of the curve order ("low-S"), as required by Bitcoin (BIP-146) and Ethereum (EIP-2). The recovery ID is returned in `recoveryId`.
  * `EC_SIGN_ED25519`: the 64-byte signature defined in RFC 8032.

Chain-specific encodings, such as DER for Bitcoin or `r || s || v` for Ethereum, are produced by the client.A base64-encoded string.  
`signerDecisions[]` |  `object (`[SignerDecision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#SignerDecision)`)` Output only. The decisions recorded so far, including the initiator's.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Transaction was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Transaction was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. The unique server-generated identifier of the Transaction.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time after which a `PENDING_AUTHORIZATION` Transaction moves to `EXPIRED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`stateMessage` |  `string` Output only. A human-readable explanation of the current state, such as why the Transaction is `SIGNING_FAILED`. May be empty.  
`metadata` |  `object (`[TransactionMetadata](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#TransactionMetadata)`)` Optional. Immutable. Caller-supplied off-chain business metadata evaluated by transaction policies.  
`action` |  `string` Required. Immutable. The requested Cedar action evaluated by transaction policies, for example `Action::"buy_transaction"`.  
`schema` |  `enum (`[PayloadSchema](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#PayloadSchema)`)` Required. Immutable. The wire format of `payload`, which selects the blockchain transaction parser used during policy evaluation.  
`payload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Immutable. The raw unsigned blockchain transaction that `signing_input` is derived from, decoded by the policy evaluator.A base64-encoded string.  
`policyEvaluationRecord` |  `object (`[PolicyEvaluationRecord](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#PolicyEvaluationRecord)`)` Output only. The transaction policy evaluation record produced when the Transaction was created.  
The payload to sign. Exactly one must be set, and it must match the Key's algorithm. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`digest` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Immutable. A pre-computed 32-byte digest to sign. Required for `EC_SIGN_SECP256K1` Keys. The client hashes the message with its chain's hash function, such as Keccak-256 for Ethereum or double SHA-256 for Bitcoin.A base64-encoded string.  
`rawMessage` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Immutable. The unhashed message to sign. Required for `EC_SIGN_ED25519` Keys, because Ed25519 (RFC 8032) hashes the message as part of signing and cannot sign a pre-computed digest.A base64-encoded string.  
End of mutually exclusive fields.  
`recoveryId` |  `integer` Output only. The recovery ID (0 or 1) of an `EC_SIGN_SECP256K1` `finalSignature`, for chains that need it, such as Ethereum's `v`. Set together with `finalSignature`. Unset for `EC_SIGN_ED25519` Keys.  
  
## State

The lifecycle state of a Transaction.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`PENDING_AUTHORIZATION` | Waiting for enough signers to authorize the Transaction.  
`SIGNING` | Enough signers authorized the Transaction and signing is in progress.  
`SIGNING_SUCCEEDED` | The Transaction is signed. `finalSignature` is set. This state is terminal.  
`SIGNING_FAILED` | Signing failed after the service's retries were exhausted, for example because of a crypto plane or TEE error. Not used when signers deny the Transaction or when it expires. `stateMessage` has details. This state is terminal.  
`REJECTED` | Enough signers denied the Transaction that the Key's thresholds can no longer be met. The Transaction will not be signed. This state is terminal.  
`EXPIRED` | The Transaction did not receive enough authorizations before `expireTime`. The Transaction will not be signed. This state is terminal.  
  
## SignerDecision

A decision recorded by one signer.

JSON representation  
---  
      
    
    {
      "user": string,
      "voteTime": string,
      "decision": enum ([Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Decision)),
      "authorizationInfo": {
        object ([AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo))
      }
    }  
  
Fields  
---  
`user` |  `string` Output only. The resource name of the User that recorded the decision. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}  
`voteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the decision was recorded.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`decision` |  `enum (`[Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Decision)`)` Output only. The decision.  
`authorizationInfo` |  `object (`[AuthorizationInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo)`)` Output only. The User's signed TransactionSigningPayload for this decision. Kept for audit.  
  
## Decision

A signer's decision on a Transaction.

Enums  
---  
`DECISION_UNSPECIFIED` | Not specified.  
`AUTHORIZE` | The signer authorizes the Transaction to be signed.  
`DENY` | The signer denies the Transaction.  
  
## TransactionMetadata

Off-chain business metadata supplied by the caller at transaction creation and projected into the Cedar policy evaluation context. The system records this client-specified metadata payload for policy evaluation but does not verify it against the transaction payload. Unset fields are omitted from the evaluation context so that any policy rule checking an omitted field does not match.

JSON representation  
---  
      
    
    {
      "fiatAmount": {
        object ([Money](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Money))
      },
      "validity": string,
      "principalValue1": string,
      "principalValue2": string
    }  
  
Fields  
---  
`fiatAmount` |  `object (`[Money](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Money)`)` Optional. Immutable. The approximate fiat value of the transaction, projected into Cedar as context.fiat_amount. At GA, currencyCode must be USD, units must be non-negative, and nanos must be 0.  
`validity` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Immutable. The duration before the transaction expires, projected into Cedar as context.validity in seconds. Must be a positive whole number of seconds when set (seconds > 0 and nanos == 0).A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`principalValue1` |  `string` Optional. Immutable. Custom caller-supplied principal attribute projected into Cedar as context.principal_value1 (maximum 256 Unicode characters).  
`principalValue2` |  `string` Optional. Immutable. Custom caller-supplied principal attribute projected into Cedar as context.principal_value2 (maximum 256 Unicode characters).  
  
## Money

Represents an amount of money with its currency type.

JSON representation  
---  
      
    
    {
      "currencyCode": string,
      "units": string,
      "nanos": integer
    }  
  
Fields  
---  
`currencyCode` |  `string` The three-letter currency code defined in ISO 4217.  
`units` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.  
`nanos` |  `integer` Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.  
  
## PayloadSchema

Wire format selector identifying the blockchain transaction parser used to decode a raw payload.

Enums  
---  
`PAYLOAD_SCHEMA_UNSPECIFIED` | Unspecified payload schema.  
`ETHEREUM_TX_V2` | Ethereum Transaction V2 (protocol-agnostic RLP / EIP-2718 envelope).  
`BITCOIN_TX_V2` | Bitcoin Transaction V2 (BIP 174 PSBT v0).  
`SOLANA_TX_V1` | Solana Transaction V1 (native SOL, SPL Token, and Token-2022 instructions).  
`EIP712_TYPED_DATA_V1` | Offline EIP-712 structured typed data (EIP-712 v1).  
  
## PolicyEvaluationRecord

Durable, immutable evaluation record produced on every transaction policy evaluation (Permit or Deny) and persisted for UI and Cloud Audit Log inspection.

JSON representation  
---  
      
    
    {
      "decision": enum ([Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Decision_1)),
      "denyReason": enum ([DenyReason](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#DenyReason)),
      "intentDigest": string,
      "policySetVersion": string,
      "evaluationContext": {
        object
      },
      "determiningPolicyIds": [
        string
      ],
      "evaluationErrors": [
        string
      ],
      "evaluationTime": string,
      "keyListMemberships": [
        {
          object ([KeyListMembership](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#KeyListMembership))
        }
      ]
    }  
  
Fields  
---  
`decision` |  `enum (`[Decision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#Decision_1)`)` Output only. The outcome of the policy evaluation (PERMIT or DENY).  
`denyReason` |  `enum (`[DenyReason](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#DenyReason)`)` Output only. The reason for denial when decision is DENY. Unset (DENY_REASON_UNSPECIFIED) when decision is PERMIT.  
`intentDigest` |  `string` Output only. Lowercase hex-encoded SHA-256 digest of the canonical transaction payload. Equals the digest signed by the Worker during the ceremony so participants can verify this exact payload was evaluated.  
`policySetVersion` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Highest activationInfo.transition_sequence or deactivationInfo.transition_sequence visible at snapshot_time. Computed by the Evaluator.  
`evaluationContext` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The projected Policy Evaluation Context (standardized Core and Optional attributes) evaluated by Cedar, persisted for UI and audit inspection.  
`determiningPolicyIds[]` |  `string` Output only. Determining Cedar policy IDs from cedar.Diagnostic.Reasons: - On PERMIT: IDs of matching permit policies. - On DENY (FORBID_RULE_MATCHED): IDs of matching forbid policies. - On DENY (NO_PERMIT_RULE_MATCHED, UNRECOGNIZED_PAYLOAD, EVALUATION_ERROR): empty.  
`evaluationErrors[]` |  `string` Output only. Runtime evaluation or parser error messages recorded during evaluation.  
`evaluationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the policy evaluation was executed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`keyListMemberships[]` |  `object (`[KeyListMembership](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions#KeyListMembership)`)` Output only. Key List memberships resolved during evaluation.  
  
## Decision

Represents the result of the transaction policy evaluation.

Enums  
---  
`DECISION_UNSPECIFIED` | Unspecified decision.  
`PERMIT` | The transaction is permitted by the active policy set.  
`DENY` | The transaction is denied by the active policy set.  
  
## DenyReason

Distinguishes why a DENY verdict occurred. Unset on PERMIT.

Enums  
---  
`DENY_REASON_UNSPECIFIED` | Unspecified deny reason (set when decision is PERMIT).  
`FORBID_RULE_MATCHED` | One or more Cedar forbid rules matched; determiningPolicyIds lists them.  
`NO_PERMIT_RULE_MATCHED` | No permit rule matched and no forbid rule or evaluation error occurred; determiningPolicyIds is empty.  
`UNRECOGNIZED_PAYLOAD` | Native transaction parser failed to decode the payload.  
`EVALUATION_ERROR` | No permit rule matched and one or more rules encountered a Cedar runtime evaluation error (e.g., referencing an optional field absent from the transaction context).  
  
## KeyListMembership

Records a Key List membership check resolved at snapshot_time. Because Key Lists are mutable, resolved membership is persisted on the evaluation record rather than reconstructed later.

JSON representation  
---  
      
    
    {
      "keyList": string,
      "address": string,
      "isMember": boolean,
      "matchedEntry": string
    }  
  
Fields  
---  
`keyList` |  `string` Output only. The Key List resource name evaluated. Format: projects/{project}/locations/{location}/instances/{instance}/keyLists/{keyList}  
`address` |  `string` Output only. The blockchain address tested against the Key List.  
`isMember` |  `boolean` Output only. Whether address resolved as a member of keyList at snapshot_time.  
`matchedEntry` |  `string` Output only. The entry in keyList that matched address (manual address, MPC Key resource name, or KeyRing resource name expansion). Empty when isMember is false.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/create)`

|  Creates a new Transaction for a Key.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/get)`

|  Gets details of a single Transaction.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/list)`

|  Lists Transactions for a Key, or across Keys.  
  
### `[recordSignerDecision](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys.transactions/recordSignerDecision)`

|  Records a signer's decision to authorize or deny a Transaction.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

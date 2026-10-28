---
url: https://docs.cloud.google.com/multi-party-compute/policy-evaluation-v1alpha/
title: Policy evaluation with Cedar \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:41.020180+00:00
---

# Policy evaluation with Cedar  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/policy-evaluation-v1alpha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)



#  Policy evaluation with Cedar Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This page covers the deprecated `v1alpha1` API and will be removed in December 2026. For the `v1beta` API, see [Transaction policy evaluation](https://docs.cloud.google.com/multi-party-compute/policy-evaluation).

This page describes how the Multi-Party Compute (MPC) Policy Engine evaluates transaction policies written in the Cedar policy language, handles cross-chain scenarios, and resolves optional or omitted metadata fields.

## Core Evaluation Principles

The Policy Engine uses the [Cedar Policy Language](https://docs.cedarpolicy.com/) to authorize cryptographic signing operations. The engine evaluates policies deterministically using three fundamental axioms:

  1. **Default Deny** : All operations are implicitly denied. For an operation to be permitted, it must match at least one active `permit` policy. If no matching `permit` policy is found, the final decision is `DENY`.
  2. **Explicit Forbid** : A `forbid` policy acts as an absolute override. If an operation matches any active `forbid` policy, the decision is immediately resolved to `DENY`, regardless of any matching `permit` policies that would otherwise allow the operation.
  3. **Missing Fields Just Mean "No Match" (Skip)** : If a rule looks for a field that is not present in the transaction payload (such as an optional field that was left out), Cedar does not crash. It treats that specific rule as a "no match" (evaluates to false) and moves on to the next rule.



* * *

## Logical Evaluation Matrix

The following table demonstrates how the Policy Engine evaluates rule combinations. 

For all scenarios, assume:

  * The transaction caller (represented as the **principal** in Cedar policies) is Alice (`User::"alice"`). In Multi-Party Compute, a principal represents the persona or identity requesting authorization for a cryptographic signing operation (such as a human signer, an automated service client, or a backend system account).
  * The transaction is transferring exactly **1 ETH** (represented as **1,000,000,000 scaled nanocoin units** in `context.transaction.spend_amount_scaled`).

Scenario | Active Policies | Result | Reason  
---|---|---|---  
**Scenario 1: Empty state** | No active policies. | `DENY` | By default, all operations are blocked unless explicitly allowed by a matching `permit` policy.  
**Scenario 2: Single permit match** | 
    
    
    permit(
      principal == User::"alice",
      action,
      resource
    )
    when {
      context.transaction.spend_amount_scaled < 10000000000
    };

_Allows up to 10 ETH_ | `PERMIT` | The transaction parameters satisfy the policy condition. Since there are no conflicting `forbid` policies, the request is allowed.  
**Scenario 3: Single permit mismatch** | 
    
    
    permit(
      principal == User::"alice",
      action,
      resource
    )
    when {
      context.transaction.spend_amount_scaled < 500000000
    };

_Allows up to 0.5 ETH_ | `DENY` | The transfer amount (1 ETH) exceeds the policy limit. Since no matching `permit` rules are met, the default deny blocks the transaction.  
**Scenario 4: Multiple permit policies** |  **Policy A:**
    
    
    permit(
      principal == User::"alice",
      action,
      resource
    )
    when {
      context.transaction.spend_amount_scaled < 500000000
    };

_Allows up to 0.5 ETH_ **Policy B:**
    
    
    permit(
      principal == User::"alice",
      action,
      resource
    )
    when {
      context.transaction.spend_amount_scaled < 5000000000
    };

_Allows up to 5 ETH_ | `PERMIT` | Although Policy A does not match, Policy B matches. You only need one matching `permit` policy to allow the transaction.  
**Scenario 5: Permit and forbid conflict** |  **Policy A (permit):**
    
    
    permit(
      principal == User::"alice",
      action,
      resource
    )
    when {
      context.transaction.spend_amount_scaled < 5000000000
    };

_Allows up to 5 ETH_ **Policy B (forbid):**
    
    
    forbid(
      principal == User::"alice",
      action,
      resource
    )
    when {
      context.transaction.recipient == "0xBlockedAddress"
    };

_Assumes destination is`0xBlockedAddress`_ | `DENY` | The transfer is sent to `0xBlockedAddress`. Even though Policy A permits the transaction amount, the destination matches the criteria for Policy B. The explicit `forbid` rule overrides Policy A and blocks the transaction.  
**Scenario 6: Unmatched forbid policy** |  Same policies as in the preceding scenario | `PERMIT` | The transfer is sent to a safe address (e.g., `0xSafeAddress`). Policy A matches successfully, and Policy B does not match because the destination is not `0xBlockedAddress`. In the absence of a matching forbid rule, the permit rule is applied.  
  
* * *

## Multi-chain and optional-field scenarios

While the preceding matrix demonstrates the core logical precedence of permitted and forbidden rules, the following scenarios illustrate how the Policy Engine evaluates rules in a multi-chain environment: specifically when executing against optional fields or different blockchain network schemas.

> **Note:** **Zero-Value Data Normalization** To prevent unexpected evaluation errors and ensure policy predictability, the Policy Engine's parsing layer normalizes unpopulated string and byte fields in the evaluation context to their type-specific zero-values (such as an empty string `""` or an empty byte array) instead of omitting them.
> 
> This behavior lets you draft explicit policies targeting unpopulated fields without risking Cedar evaluation errors. However, accessing fields that are completely undefined in a blockchain's schema (such as EVM-only `gas_limit` on a Bitcoin transaction, or Bitcoin-only `outputs` on an EVM transaction) will result in a Cedar evaluation error on that specific policy, causing it to evaluate to `false` (no match) and safely fail closed.

### Scenario 7: Cross-chain policy evaluation and unmapped schema attributes

  * **Context:** A caller submits a Bitcoin transaction. However, the active policy set contains an Ethereum-specific policy:
        
        permit(
          principal == User::"alice",
          action,
          resource
        )
        when {
          context.transaction.schema == "ethereum.transaction.v2" &&
          context.transaction.gas_limit < 100000
        };
        

  * **Result:** `DENY`

  * **Reason:** Universal intent attributes (such as `spend_amount_scaled`, `recipient`, and `max_fee_atomic`) evaluate consistently across both Ethereum and Bitcoin transactions. When a policy references chain-specific attributes that don't exist in the submitted transaction's schema (such as `gas_limit` on a Bitcoin transaction), Cedar treats the unmatched attribute as an evaluation failure, resolving that specific policy to `false` (no match) without halting the engine. Since no other active `permit` policy matches the Bitcoin transaction, the operation is denied by default.




### Scenario 8: Missing optional field in a `permit` policy

  * **Context:** A caller submits a standard ETH transfer (which does not use smart contracts). The active policy set contains a rule checking contract interactions:
        
        permit(
          principal == User::"alice",
          action,
          resource
        )
        when {
          context.transaction.asset_contract_address == "0x1111111111111111111111111111111111111111"
        };
        

  * **Result:** `DENY`

  * **Reason:** For a standard ETH transfer, the optional `asset_contract_address` is unpopulated. The parser normalizes this to the zero-value empty string `""` in the evaluation context. Evaluating the comparison `"" == "0x1111..."` returns `false` (no match) rather than raising an error. Since no other policy permits the transfer, the operation is denied by default.




### Scenario 9: Missing optional field in a `forbid` policy

  * **Context:** A caller submits a standard ETH transfer of 10 ETH. The policy set consists of:

    * **Policy A (permit):**
          
          permit(
            principal == User::"alice",
            action,
            resource
          )
          when {
            context.transaction.spend_amount_scaled <= 100000000000
          };
          

    * **Policy B (forbid):**
          
          forbid(
            principal == User::"alice",
            action,
            resource
          )
          when {
            context.transaction.asset_contract_address == "0xBannedContract"
          };
          

  * **Result:** `PERMIT`

  * **Reason:** Policy A matches successfully because 10 ETH is under the limit. Policy B checks if the contract address matches a banned address. Due to zero-value normalization, the unpopulated contract address resolves to `""`. Evaluating the comparison `"" == "0xBannedContract"` returns `false`. Since the forbid policy does not match and the permit policy does, the transaction is permitted.




### Scenario 10: Explicit checking of empty or missing fields

  * **Context:** A caller submits a standard ETH transfer (which is not sent to a smart contract). The policy set consists of:

    * **Policy A (permit):**
          
          permit(
            principal == User::"alice",
            action,
            resource
          )
          when {
            context.transaction.spend_amount_scaled <= 1000000000000
          };
          

    * **Policy B (forbid):**
          
          forbid(
            principal == User::"alice",
            action,
            resource
          )
          when {
            context.transaction.asset_contract_address == ""
          };
          

  * **Result:** `DENY`

  * **Reason:** Due to parser normalization, the missing `asset_contract_address` is presented in the evaluation context as an empty string `""`. Evaluating Policy B resolves the condition to `true` (`"" == ""`). The `forbid` policy matches, and the transaction is denied.




* * *

## Pre-Evaluation Validation (Fail-Fast Gate)

The Policy Engine enforces strict data validation. Before a payload is passed to Cedar for policy evaluation, the underlying parser validates transaction structure, RLP encoding, and cryptographic integrity.

### Scenario 11: Malformed and invalid transaction payloads

  * **Context:** A client submits a malformed byte sequence, a payload with invalid structure, or a transaction missing mandatory cryptographic fields (e.g. an EVM transaction with an invalid RLP structure or missing gas parameters).
  * **Result:** `gRPC InvalidArgument`
  * **Reason:** The internal transaction parser detects the invalid input at the API gateway layer. The operation fails closed immediately, returning a `gRPC InvalidArgument` error to the client, and evaluation by the Cedar Policy Engine is bypassed completely.



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/multi-party-compute/overview/
title: Multi-party Compute overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:36:58.761328+00:00
---

# Multi-party Compute overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Multi-party Compute overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Multi-party Compute is a Google Cloud custody platform for digital asset signing keys. It combines threshold signing, transaction policy enforcement, and enterprise governance controls.

**Note:** As of October 2026, documentation now reflects the v1beta API -- the stable, GA-intended API that will graduate to v1. For customers using the v1alpha1 API, please migrate to v1beta. If needed, refer to the now deprecated v1alpha1 [User Guide](https://docs.cloud.google.com/multi-party-compute/user-guide-v1alpha), [Security and authorization](https://docs.cloud.google.com/multi-party-compute/authorization-v1alpha), [Writing Cedar rules](https://docs.cloud.google.com/multi-party-compute/writing-rules-v1alpha), and [Policy evaluation with Cedar](https://docs.cloud.google.com/multi-party-compute/policy-evaluation-v1alpha) \-- these pages will be removed in December 2026.

## Why threshold signing

In institutional digital asset custody, a private signing key directly controls asset movement. Protecting signing keys requires mitigating three distinct security and operational risks:

  * **Cryptographic soundness** : key theft or unauthorized use lets an attacker sign fraudulent transactions, resulting in irreversible asset loss.
  * **Availability** : temporary outages or inaccessible signing infrastructure halt transaction settlement and liquidity operations.
  * **Durability** : permanent loss or corruption of key material renders the associated digital assets unrecoverable.



Centralized key management forces a tradeoff between security and operational resilience. Storing a complete private key in a single hardware security module (HSM) creates a single point of failure for availability, durability, and cryptographic soundness. Replicating that key across multiple HSMs or regions improves availability and durability, but it expands the attack surface. Because every replica holds the complete key, each copy introduces another single point of compromise.

Multi-party Compute resolves this tradeoff by using threshold signature schemes, including a hardened extension of the [DKLS23](https://eprint.iacr.org/2023/765.pdf) protocol. Independent, hardware-backed parties each generate and hold an isolated key share. During signing, these parties run a multi-party protocol to produce a valid signature without assembling the complete private key in a single location. An attacker who compromises fewer parties than the signing threshold can't forge a signature or reconstruct the key. At the same time, signing operations continue even if individual parties are unavailable or fail permanently, provided enough parties remain to meet the threshold. For more information about the protocol, see [DKLS23 cryptographic background](https://docs.cloud.google.com/multi-party-compute/crypto).

## Supported blockchains

Multi-party Compute supports the following key algorithms:

Algorithm | Curve | Typical chains  
---|---|---  
ECDSA (`EC_SIGN_SECP256K1`) | secp256k1 | Bitcoin, Ethereum, and EVM-compatible chains  
EdDSA (`EC_SIGN_ED25519`) | Ed25519 | Solana (coming soon)  
  
Once a distributed key is generated, Multi-party Compute returns its public key and the blockchain addresses derived from it.

## Enterprise controls

Multi-party Compute models your organization inside your own dedicated, isolated instance. It decides who holds key shares, how many of them must approve a signature, and which rules every transaction is evaluated against before signing.

### Users and roles

A _User_ is an identity that you onboard into an instance. Each User is bound to one principal, either a Google Account or a [Workforce Identity Federation](https://docs.cloud.google.com/multi-party-compute/byoid) principal. Each User has one or more roles:

  * **Admin** : administers Users, Teams, and other instance resources.
  * **Policy Author** : authors and approves transaction policies.
  * **Signer** : holds key shares and approves transactions.



Signers, Policy Authors, and Admins sign their approvals with an authorization key, whose private half never leaves the Customer's custody. 

On the API level, Multi-party Compute roles work together with IAM roles. IAM controls which API methods a principal can call. A User's roles control what that principal can do inside the instance. For how IAM roles and User roles work together, see [Security and authorization](https://docs.cloud.google.com/multi-party-compute/authorization).

### Teams

A _Team_ is a group of Signers, such as a department or a set of officers. Every Signer belongs to exactly one Team. Teams let a KeyPolicy refer to groups of Signers, for example, "generate key shares for 3 members of the Treasury Team, and require any 2 of them to sign" instead of naming each person.

## MPC Policies

### KeyRings and KeyPolicies

A _KeyRing_ groups keys. When you create a KeyRing, you set its _KeyPolicy_ , which defines for every key created in the KeyRing:

  * which Teams and Users hold key shares,
  * how many of them must take part to sign (the threshold), and
  * where each key share is stored (Google Cloud, customer premises, or user mobile devices).



Keys can't be moved between KeyRings or deleted. You can only disable a key, which prevents it from further signing.

### KeyLists

A _KeyList_ is a named list of blockchain addresses that transaction policies can refer to, such as trusted destinations. An entry is an existing key, a KeyRing (including keys added to it later), or an address that you enter manually.

### Transaction policies

A _transaction policy_ is a [Cedar](https://www.cedarpolicy.com/) rule that permits or forbids transactions in Multi-party Compute, for example a spending limit or an allowlist of destinations. Together, the active policies produce a verdict, permit or deny, for each transaction. The verdict guides Signers but doesn't enforce the final decision: a transaction that the automated transaction policies deny can still be executed if enough Signers approve it. 

To learn how rules are written and combined, see [Write transaction policy rules](https://docs.cloud.google.com/multi-party-compute/writing-rules) and [Transaction policy evaluation](https://docs.cloud.google.com/multi-party-compute/policy-evaluation).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

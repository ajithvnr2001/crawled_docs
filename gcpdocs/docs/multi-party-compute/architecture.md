---
url: https://docs.cloud.google.com/multi-party-compute/architecture/
title: Multi-party Compute Architecture \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:36:58.452563+00:00
---

# Multi-party Compute Architecture  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Multi-party Compute Architecture Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Google Cloud Multi-party Compute provides cryptographic trust infrastructure for institutional digital asset operations. It uses a multi-single-tenant architecture: each instance that you create is a dedicated, isolated environment with its own network ingress, its own storage, and its own hardware-isolated compute for cryptographic operations.

## Core components

![Multi-party Compute architecture diagram](https://docs.cloud.google.com/static/multi-party-compute/images/architecture-v1beta.svg)

Each Multi-party Compute instance has three main components. Governance logic, request routing, and cryptographic computations run in separate components.

### MPC API

The Multi-party Compute API manages the following resources:

  * **Users and Teams** : the identities that hold roles in the instance, and the groups of Signers that key policies refer to.
  * **KeyRings and KeyPolicies** : the KeyRings that group keys, each with the key policy that decides which Teams and Users hold key shares and how many of them must approve a signature.
  * **TransactionPolicies** : the Cedar rules that permit or forbid transactions, and the Policy Author approvals that activate or disable them.
  * **KeyLists** : the named lists of addresses that transaction policies can refer to.



The Multi-party Compute API tracks each transaction's state and the approvals recorded on it, and asks the Coordinator to orchestrate key generation and signing. Spanner stores requests and the signed approvals. Worker TEEs verify approval signatures themselves before they act on them.

### Coordinator

The Multi-party Compute API connects the Controller to the participant TEEs:

  * **Key share discovery and request routing** : it assigns healthy TEEs to hold new key shares during key generation and later routes the request to the appropriate TEEs.
  * **Health** : it monitors the participant TEEs health and works as a load balancer for the signing requests.
  * **Durability** : it manages resharing when a key share needs to be replaced.



The Coordinator does not affect the security of the protocol. It holds no key shares, and it doesn't verify approvals or policy results; that verification happens inside the participant TEEs.

### Worker TEEs

Each Worker is a TEE that runs on [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview). A Worker TEE runs two parts:

  * **Cryptographic Engine** : holds key shares and runs the secure threshold key generation and signing protocols with the other Worker TEEs.
  * **Policy Evaluator** : evaluates transactions against the active set of transaction policies.



## Transaction signing flow

In Multi-party Compute, you sign a payload with a single API call, `CreateTransaction`. Transaction policy evaluation, signer approvals, and threshold signing all start with this call. Here is the flow in a fixed order:

  1. **Request.** A Signer calls `CreateTransaction` on a key. The request carries the Signer's own approval, signed with their authorization key. IAM checks that the caller can call the method, and the request is recorded in [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).
  2. **Policy evaluation.** The transaction is evaluated against the active set of transaction policies. Policy evaluation produces a durable audit log for each verdict, either `APPROVED` or `REJECTED`.
  3. **Initiator approval.** If the initiator's approval alone meets the key policy's thresholds, `CreateTransaction` goes to Step 5 immediately.
  4. **Signer approvals.** If the initiator's approval alone doesn't meet the key policy's thresholds, the transaction enters the `PENDING_AUTHORIZATION` state. Other Signers that hold key shares of the key approve or deny the transaction using `RecordSignerDecision` call, each signed with their authorization key. The transaction waits in the `PENDING_AUTHORIZATION` state until enough Signers approve to meet the key policy's thresholds. If enough Signers deny it that the thresholds can no longer be met, the transaction moved to the `REJECTED` state. If it doesn't get enough approvals before its expiration time, it's `EXPIRED`.
  5. **Threshold signing.** When the thresholds are met, the Trusted Execution Environments (TEEs) that hold the key's shares run the threshold signing protocol and produce the signature on the transaction.

Before a participant TEE uses its key share, it checks that the exact payload it's asked to sign was evaluated against your transaction policies. No client, operator, or other service component can make a participant sign a payload that wasn't evaluated.




For the resources involved, such as Users, Teams, KeyRings, and transaction policies, see the [Multi-party Compute overview](https://docs.cloud.google.com/multi-party-compute/overview).

## Security model

  * **Key shares pinned to their TEE.** Each key share can be read only by the TEE that created it. Key shares never leave that TEE in a form that another component, including the Coordinator, the Controller, or a Google operator, can read.
  * **Customer key custody.** Customer retains full custody of their encryption keys at all times by using Cloud Key Management Service in the customer's Google Cloud Organization.
  * **Hardware isolation.** Participant TEEs run on Confidential Space, which uses hardware memory encryption to protect data in use from the host and from Google infrastructure. Attestation binds each TEE to a verified container image.
  * **E2E encryption.** The Worker TEEs communicate directly over end-to-end encrypted gRPC.
  * **Signed approvals.** Signers, Policy Authors, and Admins sign their approvals with an authorization key whose private half never leaves them. Participant TEEs verify these signatures before they sign a transaction, accept a transaction policy, or accept an Admin or Policy Author role change. This makes the transactions tamper-proof and leaves a durable audit log.
  * **Policy Author quorum.** A new transaction policy, or a request to disable one, takes effect only after the required number of Policy Authors approve it.
  * **Admin quorum.** Granting or removing the Admin or Policy Author role takes effect only after the required number of Admins approve it. For more information, see [Admin approval of role changes](https://docs.cloud.google.com/multi-party-compute/authorization#admin-approvals).



## Roadmap

The following capabilities are planned for a later releases:

  * **External TEEs** : key shares held in TEEs that customers run outside of Google Cloud, such as AWS Nitro Enclaves.
  * **Mobile key shares** : key shares held on Users' mobile devices.
  * **Resharing** : changing who holds the shares of an existing key, or replacing a lost share, without changing the key.



## System properties

The multi-party computation trust infrastructure maintains the following system properties.

### Safety (soundness in a cryptographic context)

Under all circumstances, the system must not behave in any disallowed way. For example, no group of fewer than k participants, by virtue of the [DKLS23](https://eprint.iacr.org/2023/765) protocol, is able to forge signatures. The exact security definitions are formalized in the Universal Composable framework in the literature.

When a cryptographic system is embodied in a practical implementation, care must be taken to avoid relying on assumptions that undermine the security properties. For example, each party in the protocol must be independent: their susceptibility to compromise should be independent.

To ensure this property, Multi-party Compute runs each participant in an attested TEE, and each key share is pinned to the TEE that created it. The compromise of one participant in the protocol doesn't affect the other participants.

The academic literature on multi-party computation focuses on soundness almost exclusively, and it assumes a simplistic world in which the set of parties is immutable, all parties are always available, and the parties communicate using ideal and always-available point-to-point authenticated channels. For a real-world product, several additional concerns must be addressed.

### Liveness

The system makes progress eventually. The most mundane liveness property is absence of deadlock, which holds in the [DKLS23](https://eprint.iacr.org/2023/765) protocol. A threshold key can be used for signing as long as enough of the TEEs that hold its shares are available to meet the key policy's thresholds. For example, with a 2-of-3 key, any 2 of the 3 shares can complete a signature.

### Durability

Parties that fail permanently must be replaced, otherwise the system eventually loses the shared secret permanently. For example, when hardware fails, the state of the participant running on that hardware is lost. Because key shares are pinned to their TEEs, the Coordinator tracks which TEEs hold the shares of each key. In v1beta, a key stays usable while enough of its shares remain to meet the key policy's thresholds. Replacing a lost share requires resharing, which is planned for a later release.

### Configuration changes

Both hardware failures (a TEE loses data) and organizational changes (a new hire joins the protocol with a share of the secret key) require changing who holds the shares of a key. Multi-party Compute plans to support this with a secure resharing protocol that preserves the soundness properties of [DKLS23](https://eprint.iacr.org/2023/765): a malicious new party that engages in resharing at most leaks one share of the secret, same as any other malicious party. 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

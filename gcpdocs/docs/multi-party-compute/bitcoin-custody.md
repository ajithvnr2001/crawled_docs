---
url: https://docs.cloud.google.com/multi-party-compute/bitcoin-custody/
title: Institutional Bitcoin custody on Google Cloud \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:37.976415+00:00
---

# Institutional Bitcoin custody on Google Cloud  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/bitcoin-custody/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  Institutional Bitcoin custody on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To protect institutional Bitcoin reserves without creating a single point of compromise, you can distribute signing keys across hardware-isolated enclaves by using Google Cloud Multi-party Compute. This document compares Cloud Key Management Service (Cloud KMS) and Cloud HSM with Multi-party Compute, evaluates both security models for Bitcoin custody, and presents a reference topology.

When you move Bitcoin custody to the cloud, you choose between two key management architectures:

  * **Single-key hardware security modules (HSMs)** : Cloud KMS and Cloud HSM manage static cryptographic keys inside physical HSM boundaries.
  * **Distributed threshold signing** : Multi-party Compute distributes key shares across hardware-isolated trusted execution environments (TEEs) backed by HSM root-of-trust keys.



Cloud KMS and Cloud HSM support enterprise envelope encryption and web public key infrastructure. However, they weren't designed for Bitcoin custody primitives such as hierarchical deterministic (HD) key derivation under Bitcoin Improvement Proposal 32 (BIP32), BIP340 Schnorr signing, and granular multi-party governance.

## Key challenges in cloud-based Bitcoin custody

The following table summarizes three primary challenges that you encounter when evaluating standard cloud key management services for Bitcoin custody, and how Multi-party Compute addresses each requirement.

Requirement | Limitation in Cloud KMS and Cloud HSM | How Multi-party Compute addresses this requirement  
---|---|---  
BIP32 key derivation |  Multi-tenant Cloud HSM partitions are designed for static, flat key management, such as enterprise envelope encryption. To preserve hypervisor-level security in shared cloud environments, cloud providers don't permit custom HSM firmware modules, so Cloud HSM can't compute BIP32 derivation paths natively. Because of this constraint, Cloud KMS requires flat key architectures. Applications must either track discrete key resources or derive child keys in unencrypted host memory. |  Multi-party Compute uses the linear homomorphism of the DKLS23 monotone span program to compute non-hardened BIP32 derivation paths locally. Each node independently calculates the public scalar offset tweak (`IL`) and applies that offset to its local key share with zero network communication rounds. In single-key wallets, compromising both a parent extended public key (`xpub`) and one non-hardened child private key lets an attacker calculate the parent private key. Multi-party Compute removes this exposure because child private keys (`kchild`) aren't assembled in plaintext. They exist only as distributed, ephemeral local shares (`s1'`, `s2'`) inside hardware-encrypted TEE memory.  
Single point of compromise |  The complete private key resides inside a single physical HSM boundary. A compromised authorization credential or insider threat exposes the entire wallet. |  The complete private key doesn't exist in plaintext in any single location. Key shares are mathematically distributed across independent compute nodes.  
Algorithm agility (Schnorr and Taproot) |  Physical HSM hardware cycles are slow. Adding support for elliptic curves or signature schemes such as BIP340 Schnorr on the `secp256k1` curve requires multi-year hardware recertification. |  Cryptographic operations run inside hardware-isolated Confidential VM enclaves, which lets Multi-party Compute adopt protocol updates without modifying the physical HSM boundary.  
  
## Compare Cloud KMS and Multi-party Compute

When you design digital asset signing infrastructure on Google Cloud, you can evaluate the single-key HSM model against the distributed threshold model.

### Single-key Cloud KMS and Cloud HSM model

In a Cloud KMS deployment, Cloud HSM generates an asymmetric signing key that uses the `EC_SIGN_SECP256K1_SHA256` algorithm directly inside a FIPS 140-2 Level 3 validated physical HSM. The following figure shows how an application layer interacts with Cloud HSM when deriving child keys:

![Two standard VM application layers interacting with a Cloud HSM FIPS
      140-2 Level 3 boundary, where hardened child derivation exposes the
      parent key in host memory.](https://docs.cloud.google.com/static/multi-party-compute/images/kms-key-derivation-limitations.svg)

This architecture provides managed FIPS 140-2 Level 3 validation and produces low-S normalized `secp256k1` Elliptic Curve Digital Signature Algorithm (ECDSA) signatures that the Bitcoin network accepts. However, it introduces two architectural limitations for Bitcoin custody:

  * **Key management fragmentation** : because Cloud HSM can't compute BIP32 derivation paths, your application must track millions of discrete `CryptoKey` resource IDs in Cloud KMS, removing single-root recovery workflows.
  * **Memory exposure risk** : to perform hardened derivation, your application must export the root seed into host memory, which breaks the hardware security perimeter.



### Distributed Multi-party Compute threshold model

Multi-party Compute implements a hardened extension of the [DKLS23](https://eprint.iacr.org/2023/765) threshold ECDSA protocol. Instead of generating a single complete key, independent nodes running inside Confidential Space on AMD SEV-SNP hardware-encrypted enclaves generate and hold mathematical key shares. For more information about the protocol, see [DKLS23 cryptographic background](https://docs.cloud.google.com/multi-party-compute/crypto).

The following figure shows how Multi-party Compute distributes signing across TEE nodes backed by independent HSM key encryption keys:

![Bitcoin transaction request routed to two TEE nodes that run the
      DKLS23 protocol and unwrap key shares through Cloud HSM and Cloud EKM.](https://docs.cloud.google.com/static/multi-party-compute/images/mpc-hybrid-architecture.svg)

This distributed threshold model provides three primary security benefits:

  * **No complete private key** : no single physical device, enclave, or operator holds the complete private key.
  * **Hardware-anchored root of trust** : key shares are encrypted at rest under key encryption keys (KEKs) protected by FIPS 140-2 Level 3 Cloud HSM partitions or external on-premises HSMs connected through Cloud External Key Manager.
  * **Attestation-enforced decryption** : Cloud KMS unwraps key shares into enclave memory only when a hardware attestation quote confirms that the node runs verified, untampered Multi-party Compute container images.



## Cryptographic mechanics for BIP32 and Taproot

When you evaluate threshold signing for Bitcoin custody, check that the protocol supports hierarchical address derivation and Taproot tweaking without adding inter-node network rounds.

### Non-hardened BIP32 additive derivation

BIP32 defines non-hardened child private key derivation as modular scalar addition:

\\[ k_{\text{child} } = (k_{\text{par} } + \text{parse}_{256}(I_L)) \bmod n \\]

Because Multi-party Compute uses a linear secret sharing scheme built on monotone span programs, participant nodes derive child key shares locally with zero network communication rounds. The following figure illustrates this zero-round local derivation flow:

![Node 1 and Node 2 independently computing the HMAC-SHA512 scalar tweak
      locally, updating Share 1 while keeping Share 2 unchanged, and running an
      online DKLS23 signing session.](https://docs.cloud.google.com/static/multi-party-compute/images/bip32-local-derivation-flow.svg)

### BIP341 Taproot key tweaking

This linear property also supports BIP341 Taproot key tweaking without modifying the underlying key share distribution:

\\[ Q = P + t \cdot G \quad \text{where} \quad t = H_{\text{TapTweak} }(P \parallel \text{MerkleRoot}) \\]

Before participating in the threshold signing ceremony, a participant node applies the scalar tweak (t) directly to its local key share. This capability lets you interact with Taproot script trees, Ordinals, and Discreet Log Contracts without regenerating or resharing keys.

## Architectural comparison

The following table compares Cloud KMS and Cloud HSM with Multi-party Compute across core custody dimensions.

Architectural dimension | Cloud KMS and Cloud HSM | Multi-party Compute  
---|---|---  
Cryptographic primitives | Single-signature ECDSA on the `secp256k1` curve | Threshold ECDSA (DKLS23) and threshold Edwards-curve Digital Signature Algorithm (EdDSA) on the `Ed25519` curve, extensible to threshold Schnorr on the `secp256k1` curve  
Hardware boundary | Physical PCIe HSM card | AMD SEV-SNP Confidential Space enclaves anchored to a Cloud HSM root of trust  
BIP32 HD wallet support | Manual management of discrete Cloud KMS keys | Zero-round local additive key share tweaking  
Physical key protection | FIPS 140-2 Level 3 | FIPS 140-2 Level 3 for HSM-resident KEKs that wrap key shares  
Signing latency (p95) | 20-50 ms | Less than 1,000 ms (sub-second) across distributed regions  
Affected scope of a credential breach | Complete key exposure if caller credentials or Identity and Access Management (IAM) policies are compromised | No unauthorized signing unless an attacker compromises a threshold of independent enclaves and KEKs simultaneously  
Auditability | Cloud Audit Logs | Cloud Audit Logs and Key Access Justifications hardware attestation logs  
  
## Evolution from BIP32 to threshold key management

When you design an in-house digital asset custody platform, distinguish between derivation standards created for individual hardware wallets and distributed key management designed for institutional governance. Although BIP32 is widely used for address tracking, relying on BIP32 derivation trees for security inside a multi-party computation (MPC) architecture is redundant and can add operational complexity.

### Historical context of single-seed BIP32 wallets

BIP32 was designed around the constraints of individual self-custody before threshold cryptography and hardware enclaves became widely available:

  * **Root seed dependency** : early Bitcoin custody relied on physically securing a single human-readable mnemonic phrase of 12 or 24 words.
  * **Single-backup recovery** : BIP32 HD wallets let an individual back up one seed phrase and deterministically derive addresses across multiple accounts.
  * **Single point of failure** : the root mnemonic seed represents a total single point of failure. If an attacker compromises that phrase or physical backup, every derived child private key across all accounts is exposed.



The following figure illustrates how compromising a single root seed exposes every derived child account:

![A 12- or 24-word root mnemonic seed branching to Child key 1, Child
      key 2, and Child key N, where compromising the seed exposes all derived
      child private keys.](https://docs.cloud.google.com/static/multi-party-compute/images/bip32-single-seed-vulnerability.svg)

### Remove the root seed with threshold signing

In a zero-trust institutional cloud architecture, a human-readable root mnemonic seed isn't required. Multi-party Compute eliminates the central root private key altogether. Because no complete private key exists in plaintext on any single machine or backup medium, you don't need single-phrase address recovery. Instead of deriving a key tree from one secret, Multi-party Compute distributes independent key shares across cryptographically isolated enclaves.

### Compare BIP32 derivation paths in Multi-party Compute

If your integration requires BIP32 compatibility for external address trackers or accounting workflows, compare the two technical implementation paths in the following table.

Implementation path | Cryptographic mechanism | Security and exposure profile | Latency and signing performance  
---|---|---|---  
Non-hardened BIP32 with Multi-party Compute |  Local additive tweaking: `s1' = (s1 + IL) mod n`. Each node computes the public scalar offset (`IL`) independently and applies that offset to its local key share. | 

  * **Single-key risk** : in non-MPC wallets, compromising both a parent public key (`xpub`) and one child private key lets an attacker back-calculate the parent private key.
  * **MPC mitigation** : child private keys (`kchild`) aren't assembled in plaintext and exist only as ephemeral, distributed key shares (`s1'`, `s2'`) inside hardware-encrypted TEE memory, preventing child-to-parent key recovery.

| 

  * Requires zero network communication rounds between MPC nodes to derive child keys.
  * Runs at local CPU speed before signing.
  * Supports sub-second signing latencies (p95 less than 1 second) over encrypted gRPC channels.

  
Hardened BIP32 with Multi-party Compute |  Interactive multi-party `HMAC-SHA512` hash computed over secret-shared parent key material. | 

  * Protects against child-to-parent key escalation by hashing the parent private key, which introduces substantial protocol complexity.
  * Provides no additional security benefit in a multi-party enclave environment where the parent key is already secret-shared and protected from exfiltration.

| 

  * Requires multiple interactive network rounds between MPC nodes to evaluate a threshold `HMAC-SHA512` circuit over secret-shared inputs.
  * Increases signing latency and creates transaction-processing bottlenecks.

  
  
### Recommendations for institutional custody

Multi-party Compute supports non-hardened BIP32 additive derivation for compatibility with existing systems and external address trackers. For dedicated institutional custody, consider transitioning to independent threshold keys managed directly in Multi-party Compute:

  * **Eliminate single-root dependencies** : generate, rotate, and back up independent key shares inside isolated enclaves instead of deriving keys as mathematical offsets from a single root key.
  * **Increase algorithm agility** : decouple your orchestration layer from Bitcoin-specific BIP32 derivation paths so that you can adopt non-ECDSA signature schemes, such as the `Ed25519` signature scheme for smart contract networks, under one governance model.
  * **Reduce signing complexity** : manage discrete threshold keys to simplify database lookups, keep transaction requests concise, and minimize signing latency.



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

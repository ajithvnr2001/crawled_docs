---
url: https://docs.cloud.google.com/multi-party-compute/crypto/
title: DKLS23 cryptographic background \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T23:54:37.867884+00:00
---

# DKLS23 cryptographic background  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/crypto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Guides ](https://docs.cloud.google.com/multi-party-compute/overview)



#  DKLS23 cryptographic background Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Multi-party Compute signs with two key algorithms: ECDSA on secp256k1 and EdDSA on Ed25519 (coming soon). This page covers the threshold ECDSA protocol, DKLS23, and the changes Google made to it. For the supported algorithms, see [Supported blockchains](https://docs.cloud.google.com/multi-party-compute/overview#supported-blockchains).

## Threshold ECDSA and DKLS23

In contrast to other signature schemes, the problem of threshold signing for ECDSA has been notoriously difficult. Until 2017, most solutions involved severe tradeoffs. 

In 2018, DKLS presented the first solution for 2-out-of-2 signing for ECDSA that only relied on ECDSA-based cryptographic assumptions (e.g., did not require Paillier, RSA or other different family of cryptographic hardness assumptions). The breakthrough idea in this protocol was a novel way to argue for malicious security for an MPC-based approach (prior attempts to apply generic maliciously-secure MPC techniques resulted in protocols that required minutes to execute instead of milliseconds). 

Subsequent improvements by the same authors lead to a k-out-of-n protocol, and finally the [DKLS23](https://eprint.iacr.org/2023/765) improvement led to a generic framework for 3-round k-out-of-n threshold ECDSA that captured all prior approaches, and identified the DKLS approach as the most efficient along notable performance metrics. In particular, that version of the protocol only relies on ideal commitment and two-party multiplication primitives. The resulting protocol requires single-digit milliseconds of computation per party (resulting in order of magnitude speedups over competing approaches), and importantly, it relies on simpler cryptographic primitives that only use elliptic curve operations (in contrast to expensive Paillier, homomorphic operations, and expensive zero-knowledge range proofs and proofs of well-formedness of cryptographic keys required in other works). 

The protocol has been internally evaluated by several auditors, including experts hired by Coinbase and other cryptography experts. Doerner and Roy [DR26](https://eprint.iacr.org/2026/654) recently identified one miscalculation in the security analysis for the DKLS multiplier which requires an extra 22 invocations of OT to achieve the claimed 120 bits of security. This change has been implemented. Similarly, other external auditors have pointed out missing details in the writeup of the protocol with respect to the implications of broadcast in the point-to-point channel model (notably, it is important to echo some configuration parameters to attain common knowledge).

Subsequent work at Google on the protocol has substantially hardened both the implementation, reduced the resources required to operate the protocol at scale, and extended the functionality of the scheme. For example, the academic literature under-specifies the selection and implementation of the Random oracle. While a useful academic abstraction, the implementation of the Random Oracle is a subtle task that has led to several flaws documented by security audits. 

A notable aspect of our work has been to develop a type system (based on two spawn and fork operations, as well as rigorous use of type systems to prevent copying, moving, and aliasing of pointers to oracles) to ensure that every session and subsession uses a different random oracle. 

Another important improvement relates to the selection of session and subsession identifiers. The UC model, and thus all protocols proven secure in that model, require the environment to provide fresh session identifiers. In practice, a system must ensure that the adversary cannot violate this assumption, and this usually requires participants to maintain an unbounded state for this purpose. We have augmented the original DKLS protocol with extra rounds to select this identifier in a way that only requires a constant-size state. 

Altogether, the updated and hardened protocol still completes a signing operation in tens of milliseconds.

In terms of functionality, the [DKLS23](https://eprint.iacr.org/2023/765) paper only considers the standard k-out-of-n threshold access structure. In practice, customers may require an access structure that mimics organizational rules. The cryptographic literature contains many approaches to designing access structures for secret sharing. Here, we have extended the DKLS protocol to support more general access structures that can be composed from threshold-k-out-of-n gates. This allows policies such as "2-out-of-3 of the following groups: (a) the customer, (b) 2-out-of-10 of the risk control officers, (c) 2-out-of-3 of the finance, legal, and accounting department leads", etc.

In the v1beta API, you define this access structure as the [key policy](https://docs.cloud.google.com/multi-party-compute/overview#key-policies) of a KeyRing, in the `keyPolicy` field. Every key created in the KeyRing uses it. A key policy can have at most two levels: the root threshold rule, and threshold rules directly under it. A threshold rule under the root can't contain another threshold rule.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

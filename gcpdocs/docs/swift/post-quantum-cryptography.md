---
url: https://docs.cloud.google.com/swift/post-quantum-cryptography/
title: Post-quantum cryptography (PQC) support \u00a0|\u00a0 Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T22:46:32.571216+00:00
---

# Post-quantum cryptography (PQC) support  |  Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/post-quantum-cryptography/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Post-quantum cryptography (PQC) support Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how the Google Cloud client libraries for Swift support post-quantum cryptography (PQC). PQC protects encrypted communications against potential future quantum computing capabilities that could compromise classical public-key cryptography.

## Summary

Google Cloud services and Google Front End load balancers support hybrid post-quantum key agreement (`X25519MLKEM768`, IANA group ID `0x11ec` / 4588) during TLS 1.3 handshakes.

The Google Cloud client libraries for Swift enable and negotiate post-quantum hybrid key agreement by default without requiring custom configuration.

## How PQC operates in the Swift client libraries

The Swift client libraries use either [`grpc-swift-2`](https://github.com/grpc/grpc-swift-2) or [`async-http-client`](https://github.com/swift-server/async-http-client) on GitHub, both backed by Apple's [`swift-nio-ssl`](https://github.com/apple/swift-nio-ssl) and embedded BoringSSL (`CNIOBoringSSL`).

When negotiating TLS 1.3 connections, `swift-nio-ssl` configures `X25519MLKEM768` as the first and preferred key exchange group in its default curve list:

  * `X25519MLKEM768` (hybrid post-quantum key exchange)
  * `X25519` (classical curve)
  * `secp256r1` (classical curve P-256)
  * `secp384r1` (classical curve P-384)



During the TLS 1.3 `ClientHello`, the client offers `X25519MLKEM768`. Because Google Cloud endpoints support this group, the handshake selects it, securing data in transit against retrospective decryption attacks.

If a server or intermediate network proxy doesn't support `X25519MLKEM768`, negotiation automatically and transparently falls back to classical algorithms.

## What's next

  * Read the [Post-quantum cryptography](https://cloud.google.com/security/resources/post-quantum-cryptography) guide for more information about Google Cloud's PQC support.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-04 UTC."],[],[]] 

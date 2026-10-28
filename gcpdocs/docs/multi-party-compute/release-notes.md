---
url: https://docs.cloud.google.com/multi-party-compute/release-notes/
title: Multi-party Compute release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:35.839030+00:00
---

# Multi-party Compute release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ Resources ](https://docs.cloud.google.com/multi-party-compute/locations)



#  Multi-party Compute release notes Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page documents production updates to Multi-party Compute. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 15, 2026

Feature

**Workforce Identity Federation (BYOID)** : You can now authenticate to the Multi-party Compute API with identities from your organization's external identity provider, such as Okta or Microsoft Entra ID, using Workforce Identity Federation and Workload Identity Federation. For setup steps, see [Configure Workforce Identity Federation (BYOID)](https://docs.cloud.google.com/multi-party-compute/byoid).

Feature

**Pagination for ListKeyRings and ListParticipants** : `KeyRingService.ListKeyRings` and `ParticipantService.ListParticipants` now support pagination with `page_size` and `page_token`. Responses return up to 100 results by default, and you can set `page_size` to request up to 1,000. When more results are available, the response includes a `next_page_token` that you pass as `page_token` to get the next page.

## October 01, 2026

Feature

**Schnorr Signatures for Curve25519** : Added support for generating distributed Schnorr signatures using `Curve25519` keys with standard `Ed25519` (RFC 8032) challenge hashing for multi-party transaction signing.

Feature

**Extended Participant and Approver ID Limits** : Increased character limits for external participant IDs (`external_participant_id`) and policy approver governance entity IDs (`governance_entity_id`) to 4,096 characters, enabling full Workforce Identity Federation and Workload Identity Federation principal URIs in API requests, Cedar policies, and JWS intent tokens.

Fixed

**Assent Signature Validation Error Code** : Updated `RecordParticipantDecision` in `ProposalService` to return `INVALID_ARGUMENT` instead of `PERMISSION_DENIED` when a participant's cryptographic assent or dissent signature fails verification.

Feature

**Bitcoin Policy Engine Rules** : Enhanced Bitcoin policy evaluation in the Policy Engine. Cedar rules for Bitcoin transactions now support normalized spending amounts (`spend_amount_scaled`), automated change output detection, destination address classification (such as SegWit and Taproot), and `OP_RETURN` data transactions.

## August 20, 2026

Fixed

**API Validations & Stability**: Enhanced API request validation for `AuthorizePayload`, `UpdatePolicyAuthorTrustBundle`, and quorum thresholds. Resolved a cache synchronization bug during policy activation.

Breaking

**Dissent Signature Payload Update** : Dissent signatures for the `RecordParticipantDecision` API must now be generated over the SHA-256 hash of the Proposal ID instead of the raw transaction digest. Assent signatures remain unchanged.

Feature

**Curve25519 Support** : Added support for the `Curve25519` elliptic curve for distributed key generation and signing.

Feature

**Ethereum V2 Schema** : Introduced the `ETHEREUM_TX_V2` schema for the Policy Engine to normalize EVM transaction data into a protocol-agnostic format.

Feature

**Ethereum Wallet Address Exposure** : The MPC API now automatically exposes the derived Ethereum wallet address for distributed keys generated with the `ECDSA_SECP256K1` algorithm.

Feature

**Policy Engine Bitcoin Support (Preview)** : You can now authorize Bitcoin payloads using the `BITCOIN_TX_V2` schema. This includes parsing for Partially Signed Bitcoin Transactions (PSBT v0, BIP-174) and native Bitcoin address extraction.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

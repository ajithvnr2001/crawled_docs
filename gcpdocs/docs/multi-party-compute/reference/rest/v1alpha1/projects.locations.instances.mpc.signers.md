---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers
title: REST Resource: projects.locations.instances.mpc.signers \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:45.390835+00:00
---

# REST Resource: projects.locations.instances.mpc.signers  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.mpc.signers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Participant
    * JSON representation
  * AssentKey
    * JSON representation
  * PublicKeySignatureAlgorithm
  * State
  * Methods



## Resource: Participant

Represents a participant entity in the Multi-party Compute (MPC) System. Participants are external entities (e.g., servers, individuals) that hold key shares and collaborate in cryptographic operations.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "externalParticipantId": string,
      "activePublicAssentKey": {
        object ([AssentKey](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#AssentKey))
      },
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique resource name of the Participant. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/signers/{signer}  
`displayName` |  `string` Optional. User-defined display name for the Participant.  
`externalParticipantId` |  `string` Optional. The participant's ID in some external system.  
`activePublicAssentKey` |  `object (`[AssentKey](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#AssentKey)`)` Required. AssentKey represents the public key used for assenting to proposals.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels for grouping or filtering. e.g., {"env": "production", "team": "treasury"}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Participant was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Participant was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#State)`)` Output only. The state of the participant.  
  
## AssentKey

Represents the public key used for assenting to proposals.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "algorithm": enum ([PublicKeySignatureAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#PublicKeySignatureAlgorithm))
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The public key material.A base64-encoded string.  
`algorithm` |  `enum (`[PublicKeySignatureAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#PublicKeySignatureAlgorithm)`)` Required. The algorithm associated with the public key.  
  
## PublicKeySignatureAlgorithm

Enum for PublicKeySignatureAlgorithm. Supported algorithms for public key assenting.

Enums  
---  
`PUBLIC_KEY_SIGNATURE_ALGORITHM_UNSPECIFIED` | Not specified.  
`PUBLIC_KEY_SIGNATURE_ALGORITHM_ECDSA_SECP256K1` | ECDSA on curve secp256k1.  
  
## State

The state of the participant.

Enums  
---  
`STATE_UNSPECIFIED` | State is unspecified.  
`ACTIVE` | The participant is active and can be used in key ceremonies.  
`INACTIVE` | The participant is inactive and cannot be used in key ceremonies.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/create)`

|  Registers a new participant entity capable of holding key shares.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/get)`

|  Gets details of a single Participant.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/list)`

|  Lists Participants in a given project and location.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 

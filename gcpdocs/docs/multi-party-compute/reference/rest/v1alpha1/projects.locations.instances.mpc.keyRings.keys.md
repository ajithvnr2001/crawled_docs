---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys
title: REST Resource: projects.locations.instances.mpc.keyRings.keys \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:37.527241+00:00
---

# REST Resource: projects.locations.instances.mpc.keyRings.keys  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.mpc.keyRings.keys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Key
    * JSON representation
  * KeyAlgorithm
  * ParticipantShare
    * JSON representation
  * State
  * BlockchainAddresses
    * JSON representation
  * Secp256k1Addresses
    * JSON representation
  * Methods



## Resource: Key

Represents a distributed Multi-party Compute (MPC) key.

JSON representation  
---  
      
    
    {
      "name": string,
      "threshold": integer,
      "algorithm": enum ([KeyAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#KeyAlgorithm)),
      "participantShares": [
        {
          object ([ParticipantShare](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#ParticipantShare))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#State)),
      "publicKey": string,
      "blockchainAddresses": {
        object ([BlockchainAddresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#BlockchainAddresses))
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique resource name of the Key. This field is server-assigned and follows the format required by AIP-122: projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyRing}/keys/{key}  
`threshold` |  `integer` Required. The number of participant assents required for this key to sign.  
`algorithm` |  `enum (`[KeyAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#KeyAlgorithm)`)` Required. The cryptographic algorithm used by this key.  
`participantShares[]` |  `object (`[ParticipantShare](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#ParticipantShare)`)` Required. The list of participants and their respective key share information. The participantId for each entry must be provided on creation.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels for grouping or filtering. e.g., {"env": "production", "team": "treasury"}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#State)`)` Output only. The state of the key.  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The combined public key. Populated after DKG completes. Note: This is an uncompressed raw public key (e.g., 65 bytes starting with 0x04 for secp256k1). Because the field type is `bytes`, JSON/REST clients will see this value encoded as a Base64 string due to standard Protobuf JSON transcoding.A base64-encoded string.  
`blockchainAddresses` |  `object (`[BlockchainAddresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#BlockchainAddresses)`)` Output only. Addresses derived from the public key.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Key was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Key was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## KeyAlgorithm

The cryptographic algorithm used by the key.

Enums  
---  
`KEY_ALGORITHM_UNSPECIFIED` | Unspecified algorithm.  
`ECDSA_SECP256K1` | ECDSA on curve secp256k1.  
  
## ParticipantShare

Represents a participant's assigned share of the key.

JSON representation  
---  
      
    
    {
      "participantId": string,
      "shareIndex": integer,
      "gcsObjectPath": string
    }  
  
Fields  
---  
`participantId` |  `string` Required. Immutable. The participant ID. Must be provided on keys.create.  
`shareIndex` |  `integer` Output only. The index of the key share in the threshold scheme.  
`gcsObjectPath` |  `string` Output only. The Cloud Storage object path where the encrypted key share is durably stored.  
  
## State

The state of the key.

Enums  
---  
`STATE_UNSPECIFIED` | State is unspecified.  
`CREATING` | The key resource has been initialized by a keys.create request. The system is currently orchestrating the distributed key generation ceremony. This is a transient state; no cryptographic operations can be performed with the key yet.  
`ACTIVE` | The DKG ceremony has successfully completed. The public key has been generated and populated in the resource, and all key shares are securely stored. The key is now fully operational and available for use in signing proposals. This is the steady state for a healthy key.  
`DISABLED` | The key has been administratively disabled via an keys.patch operation. While the key material and history remain intact, the service will reject any new attempts to use this key for signing proposals. This state is used for temporary suspensions or as a prelude to key rotation/retirement.  
`FAILED` | The DKG ceremony encountered an unrecoverable error (e.g., repeated worker failures or timeouts). The key generation process has been aborted, and no usable key material exists. This is a terminal failure state; the resource cannot be transitioned to ACTIVE.  
  
## BlockchainAddresses

Addresses derived from the public key, organized by curve.

JSON representation  
---  
      
    
    {
    
      // Union field curve_addresses can be only one of the following:
      "secp256k1Addresses": {
        object ([Secp256k1Addresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#Secp256k1Addresses))
      }
      // End of list of possible types for union field curve_addresses.
    }  
  
Fields  
---  
Union field `curve_addresses`. The addresses derived from the public key, organized by curve. `curve_addresses` can be only one of the following:  
`secp256k1Addresses` |  `object (`[Secp256k1Addresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#Secp256k1Addresses)`)` Output only. Addresses derived from a SECP256K1 public key.  
  
## Secp256k1Addresses

Addresses derived from a SECP256K1 public key.

JSON representation  
---  
      
    
    {
      "ethereumAddress": string
    }  
  
Fields  
---  
`ethereumAddress` |  `string` Output only. The Ethereum address derived from the public key, provided for convenience. Formatted as a hex string with a `0x` prefix.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/create)`

|  Initiates a Distributed Key Generation (DKG) ceremony.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/get)`

|  Gets details of a single Key.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/list)`

|  Lists Keys in a given KeyRing.  
  
### `[patch](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/patch)`

|  Updates a Key.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-20 UTC."],[],[]] 

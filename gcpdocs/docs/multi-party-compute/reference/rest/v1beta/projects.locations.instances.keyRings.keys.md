---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys
title: REST Resource: projects.locations.instances.keyRings.keys \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:50.755871+00:00
---

# REST Resource: projects.locations.instances.keyRings.keys  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.keyRings.keys Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Key
    * JSON representation
  * KeyAlgorithm
  * KeySpec
    * JSON representation
  * UserKeyShares
    * JSON representation
  * KeyShareNode
    * JSON representation
  * State
  * PublicKeyInfo
    * JSON representation
  * BlockchainAddresses
    * JSON representation
  * Secp256k1Addresses
    * JSON representation
  * BitcoinAddresses
    * JSON representation
  * Ed25519Addresses
    * JSON representation
  * Methods



## Resource: Key

A Key is a cryptographic key pair generated and used through threshold MPC. The private key never exists in one place: it is split into key shares held by Users, as defined by the KeyPolicy of the parent KeyRing.

Keys cannot be deleted or moved between KeyRings. They can only be disabled.

JSON representation  
---  
      
    
    {
      "name": string,
      "algorithm": enum ([KeyAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeyAlgorithm)),
      "keyShares": {
        object ([KeySpec](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeySpec))
      },
      "state": enum ([State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#State)),
      "publicKeyInfo": {
        object ([PublicKeyInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#PublicKeyInfo))
      },
      "createTime": string,
      "updateTime": string,
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Key. Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}/keys/{key}  
`algorithm` |  `enum (`[KeyAlgorithm](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeyAlgorithm)`)` Required. Immutable. The signing algorithm of the Key.  
`keyShares` |  `object (`[KeySpec](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeySpec)`)` Output only. The Users that hold the Key's key shares, and the thresholds needed to sign. The server fills this from the parent KeyRing's KeyPolicy when the Key is created.  
`state` |  `enum (`[State](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#State)`)` Output only. The lifecycle state of the Key.  
`publicKeyInfo` |  `object (`[PublicKeyInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#PublicKeyInfo)`)` Output only. The public key and derived addresses. Set once the Key is `ACTIVE`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Key was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the Key was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. The unique server-generated identifier of the Key.  
  
## KeyAlgorithm

The signing algorithm of a Key.

Enums  
---  
`KEY_ALGORITHM_UNSPECIFIED` | Not specified.  
`EC_SIGN_SECP256K1` | ECDSA on curve secp256k1 (Bitcoin, Ethereum, and EVM-compatible chains).  
`EC_SIGN_ED25519` | EdDSA on curve Ed25519 (Solana, NEAR, Cardano, Sui).  
  
## KeySpec

A node in the tree of key-share holders.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userKeyShares": {
        object ([UserKeyShares](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#UserKeyShares))
      },
      "keyShareNode": {
        object ([KeyShareNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeyShareNode))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The kind of node. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userKeyShares` |  `object (`[UserKeyShares](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#UserKeyShares)`)` Output only. The key shares held by one User.  
`keyShareNode` |  `object (`[KeyShareNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeyShareNode)`)` Output only. A nested threshold rule over child nodes.  
End of mutually exclusive fields.  
  
## UserKeyShares

The key shares one User holds for a Key, resolved from a KeyPolicy `UserNode` or `TeamNode` when the Key was created.

JSON representation  
---  
      
    
    {
      "user": string,
      "threshold": integer,
      "shareStorage": [
        {
          object ([StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo))
        }
      ]
    }  
  
Fields  
---  
`user` |  `string` Output only. The resource name of the User that holds the key shares. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}  
`threshold` |  `integer` Output only. The number of this User's key shares needed to sign. Currently always 1.  
`shareStorage[]` |  `object (`[StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo)`)` Output only. Where each of the User's key shares is stored, one entry per key share. Currently always exactly one entry.  
  
## KeyShareNode

A k-of-n threshold rule over child nodes, resolved from the KeyPolicy when the Key was created.

JSON representation  
---  
      
    
    {
      "keyShareNodeId": string,
      "threshold": integer,
      "subKeyShares": [
        {
          object ([KeySpec](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeySpec))
        }
      ],
      "storageInfo": {
        object ([StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo))
      }
    }  
  
Fields  
---  
`keyShareNodeId` |  `string` Output only. The `policyNodeId` of the KeyPolicy `PolicyNode` this node was resolved from. Empty if the node was resolved from a `TeamNode` or `UserNode`.  
`threshold` |  `integer` Output only. The number of children in `subKeyShares` needed to sign.  
`subKeyShares[]` |  `object (`[KeySpec](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#KeySpec)`)` Output only. The child nodes.  
`storageInfo` |  `object (`[StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo)`)` Output only. Where the key shares under this node are stored.  
  
## State

The lifecycle state of a Key.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`CREATING` | Distributed key generation is in progress. The Key cannot sign yet.  
`ACTIVE` | Distributed key generation succeeded. The Key can sign.  
`DISABLED` | The Key is disabled and cannot sign. Its key shares are kept.  
`FAILED` | Distributed key generation failed. No usable key material exists. This state is terminal.  
  
## PublicKeyInfo

The public half of the Key and the addresses derived from it.

JSON representation  
---  
      
    
    {
      "publicKey": string,
      "blockchainAddresses": {
        object ([BlockchainAddresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#BlockchainAddresses))
      }
    }  
  
Fields  
---  
`publicKey` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The public key. For `EC_SIGN_SECP256K1` this is the 65-byte uncompressed point starting with `0x04`. For `EC_SIGN_ED25519` this is the 32-byte encoded point.A base64-encoded string.  
`blockchainAddresses` |  `object (`[BlockchainAddresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#BlockchainAddresses)`)` Output only. Blockchain addresses derived from `publicKey`.  
  
## BlockchainAddresses

Blockchain addresses derived from a public key, grouped by curve.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "secp256k1Addresses": {
        object ([Secp256k1Addresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#Secp256k1Addresses))
      },
      "ed25519Addresses": {
        object ([Ed25519Addresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#Ed25519Addresses))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The addresses for the key's curve. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`secp256k1Addresses` |  `object (`[Secp256k1Addresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#Secp256k1Addresses)`)` Output only. Addresses derived from a SECP256K1 public key.  
`ed25519Addresses` |  `object (`[Ed25519Addresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#Ed25519Addresses)`)` Output only. Addresses derived from an Ed25519 public key.  
End of mutually exclusive fields.  
  
## Secp256k1Addresses

Addresses derived from a SECP256K1 public key.

JSON representation  
---  
      
    
    {
      "ethereumAddress": string,
      "bitcoinMainnetAddresses": {
        object ([BitcoinAddresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#BitcoinAddresses))
      }
    }  
  
Fields  
---  
`ethereumAddress` |  `string` Output only. The Ethereum address derived from the public key. Formatted as a hex string with a `0x` prefix.  
`bitcoinMainnetAddresses` |  `object (`[BitcoinAddresses](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys#BitcoinAddresses)`)` Output only. The Bitcoin mainnet addresses derived from the public key.  
  
## BitcoinAddresses

Single-key Bitcoin addresses derived from the compressed SECP256K1 public key. Taproot (P2TR) addresses are not included because they require Schnorr signatures.

JSON representation  
---  
      
    
    {
      "p2wpkhAddress": string,
      "p2shP2wpkhAddress": string,
      "p2pkhAddress": string
    }  
  
Fields  
---  
`p2wpkhAddress` |  `string` Output only. The native SegWit (P2WPKH) address. Formatted as a bech32 string, e.g. `bc1q...`.  
`p2shP2wpkhAddress` |  `string` Output only. The nested SegWit (P2SH-P2WPKH) address. Formatted as a base58check string, e.g. `3...`.  
`p2pkhAddress` |  `string` Output only. The legacy (P2PKH) address. Formatted as a base58check string, e.g. `1...`.  
  
## Ed25519Addresses

Addresses derived from an Ed25519 public key.

JSON representation  
---  
      
    
    {
      "solanaAddress": string
    }  
  
Fields  
---  
`solanaAddress` |  `string` Output only. The Solana address derived from the public key. Formatted as a base58 string.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/create)`

|  Creates a new Key in a KeyRing by running distributed key generation (DKG).  
  
### `[disable](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/disable)`

|  Disables a Key so it can no longer sign.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/get)`

|  Gets details of a single Key.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings.keys/list)`

|  Lists Keys in a KeyRing.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

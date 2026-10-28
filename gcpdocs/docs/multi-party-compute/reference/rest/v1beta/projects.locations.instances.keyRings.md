---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings
title: REST Resource: projects.locations.instances.keyRings \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:30.578053+00:00
---

# REST Resource: projects.locations.instances.keyRings  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.keyRings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: KeyRing
    * JSON representation
  * KeyPolicy
    * JSON representation
  * PolicyNode
    * JSON representation
  * ParticipantNode
    * JSON representation
  * TeamNode
    * JSON representation
  * UserNode
    * JSON representation
  * Methods



## Resource: KeyRing

A KeyRing is a logical grouping of keys. Every KeyRing has its own KeyPolicy, set when the KeyRing is created, and every key created in the KeyRing follows it.

Keys cannot be moved between KeyRings, and a KeyRing can only be deleted when it contains no keys.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "keyPolicy": {
        object ([KeyPolicy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#KeyPolicy))
      },
      "createTime": string,
      "updateTime": string,
      "uid": string,
      "keyCount": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the KeyRing. Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}  
`displayName` |  `string` Optional. User-assigned display name for the KeyRing.  
`keyPolicy` |  `object (`[KeyPolicy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#KeyPolicy)`)` Required. Immutable. The KeyPolicy that every key in this KeyRing follows. Set only when the KeyRing is created. It belongs to this KeyRing alone and cannot be shared with or referenced by other KeyRings.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the KeyRing was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the KeyRing was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. The unique server-generated identifier of the KeyRing.  
`keyCount` |  `integer` Output only. The number of keys in the KeyRing, including disabled keys. Because keys are never deleted, a KeyRing can be deleted only while this is 0.  
  
## KeyPolicy

A KeyPolicy defines how key shares are allocated when a key is generated: who holds them, how many are needed to sign, and where they are stored.

A KeyPolicy is a tree of threshold rules. The root is a `PolicyNode` that requires `threshold` of its children. Each child is a `TeamNode`, a `UserNode`, or a nested `PolicyNode`. The tree is limited to two levels: a `PolicyNode` nested under the root cannot contain another `PolicyNode`.

A KeyPolicy is not a standalone resource. It is set inline on a KeyRing when the KeyRing is created, belongs only to that KeyRing, and cannot be changed or shared. To use different rules for new keys, create a new KeyRing with a new KeyPolicy.

JSON representation  
---  
      
    
    {
      "policy": {
        object ([PolicyNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#PolicyNode))
      }
    }  
  
Fields  
---  
`policy` |  `object (`[PolicyNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#PolicyNode)`)` Required. Immutable. The root threshold rule.  
  
## PolicyNode

A k-of-n threshold rule over child nodes.

JSON representation  
---  
      
    
    {
      "policyNodeId": string,
      "threshold": integer,
      "subKeyShares": [
        {
          object ([ParticipantNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#ParticipantNode))
        }
      ]
    }  
  
Fields  
---  
`policyNodeId` |  `string` Required. An identifier for this node, unique within the KeyPolicy. Keys refer to it when they report which key shares fill which slot. Must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.  
`threshold` |  `integer` Required. The number of children in `subKeyShares` that must be satisfied to sign. Must be between 1 and the size of `subKeyShares`.  
`subKeyShares[]` |  `object (`[ParticipantNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#ParticipantNode)`)` Required. The child nodes. Must contain at least one node.  
  
## ParticipantNode

A child of a `PolicyNode`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "teamNode": {
        object ([TeamNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#TeamNode))
      },
      "userNode": {
        object ([UserNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#UserNode))
      },
      "policyNode": {
        object ([PolicyNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#PolicyNode))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The kind of participant. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`teamNode` |  `object (`[TeamNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#TeamNode)`)` `threshold` of `totalMembers` key shares held by members of a Team.  
`userNode` |  `object (`[UserNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#UserNode)`)` Key shares held by a specific User.  
`policyNode` |  `object (`[PolicyNode](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings#PolicyNode)`)` A nested threshold rule. Only allowed directly under the root.  
End of mutually exclusive fields.  
  
## TeamNode

A threshold rule over members of a Team. When a key is created, `totalMembers` members of the Team each receive a key share, and any `threshold` of them can sign.

JSON representation  
---  
      
    
    {
      "team": string,
      "threshold": integer,
      "totalMembers": integer,
      "storageInfo": {
        object ([StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo))
      }
    }  
  
Fields  
---  
`team` |  `string` Required. The resource name of the Team. Format: projects/{project}/locations/{location}/instances/{instance}/teams/{team}  
`threshold` |  `integer` Required. The number of key shares from this Team needed to sign. Must be between 1 and `totalMembers`.  
`totalMembers` |  `integer` Required. The number of Team members that receive a key share. This is not the size of the Team: the Team may have more members than this. Key creation fails if the Team has fewer active signers than this.  
`storageInfo` |  `object (`[StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo)`)` Required. Where the Team's key shares are stored.  
  
## UserNode

Key shares held by a specific User. The User must have the `SIGNER` role.

JSON representation  
---  
      
    
    {
      "user": string,
      "shareStorage": [
        {
          object ([StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo))
        }
      ],
      "threshold": integer
    }  
  
Fields  
---  
`user` |  `string` Required. The resource name of the User. Format: projects/{project}/locations/{location}/instances/{instance}/users/{user}  
`shareStorage[]` |  `object (`[StorageInfo](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo)`)` Required. Where each of the User's key shares is stored, one entry per key share. Currently must contain exactly one entry with `storageType` set to `GCP_TEE`.  
`threshold` |  `integer` Required. The number of this User's key shares needed to sign. Must be between 1 and the size of `shareStorage`. Currently must be 1.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/create)`

|  Creates a new KeyRing in an instance.  
  
### `[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/delete)`

|  Deletes a KeyRing and its KeyPolicy.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/get)`

|  Gets details of a single KeyRing.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyRings/list)`

|  Lists KeyRings in an instance.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

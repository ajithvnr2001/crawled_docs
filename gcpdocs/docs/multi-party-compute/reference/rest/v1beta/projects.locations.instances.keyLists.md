---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists
title: REST Resource: projects.locations.instances.keyLists \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:30.374187+00:00
---

# REST Resource: projects.locations.instances.keyLists  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  REST Resource: projects.locations.instances.keyLists Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: KeyList
    * JSON representation
  * Entry
    * JSON representation
  * ManualEntry
    * JSON representation
  * Methods



## Resource: KeyList

A KeyList is a named list of blockchain addresses that transaction policies can reference, for example as a list of trusted destinations.

Each entry is a Key, a KeyRing, or a manually entered address. A KeyRing entry covers every Key in the KeyRing, including Keys created after the entry was added.

Entries are changed only with `keyLists.addEntries` and `keyLists.removeEntries`.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "entries": [
        {
          object ([Entry](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists#Entry))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the KeyList. Format: projects/{project}/locations/{location}/instances/{instance}/keyLists/{keyList}  
`displayName` |  `string` Optional. User-assigned display name for the KeyList.  
`description` |  `string` Optional. User-provided description of the KeyList.  
`entries[]` |  `object (`[Entry](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists#Entry)`)` Optional. The entries in the KeyList. Can be set when the KeyList is created; after that, change them with `keyLists.addEntries` and `keyLists.removeEntries`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the KeyList was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the KeyList was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. The unique server-generated identifier of the KeyList.  
  
## Entry

One entry in a KeyList.

JSON representation  
---  
      
    
    {
      "addTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "manualEntry": {
        object ([ManualEntry](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists#ManualEntry))
      },
      "keyRing": string,
      "key": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`addTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the entry was added to the KeyList.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
What the entry refers to. Exactly one must be set. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`manualEntry` |  `object (`[ManualEntry](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists#ManualEntry)`)` A manually entered address, typically one not managed by this instance.  
`keyRing` |  `string` The resource name of a KeyRing in the same instance. Covers every Key in the KeyRing. Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}  
`key` |  `string` The resource name of a Key in the same instance. Format: projects/{project}/locations/{location}/instances/{instance}/keyRings/{keyRing}/keys/{key}  
End of mutually exclusive fields.  
  
## ManualEntry

A manually entered blockchain address.

JSON representation  
---  
      
    
    {
      "address": string,
      "source": string,
      "reason": string
    }  
  
Fields  
---  
`address` |  `string` Required. The blockchain address, in the chain's usual text form (for example, a `0x`-prefixed hex string for Ethereum). Two manual entries with the same address are the same entry.  
`source` |  `string` Optional. Where the address came from, for example the name of an exchange or an internal ticket.  
`reason` |  `string` Optional. Why the address is in the KeyList.  
  
## Methods  
  
---  
  
### `[addEntries](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/addEntries)`

|  Adds entries to a KeyList and returns the updated KeyList.  
  
### `[create](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/create)`

|  Creates a new KeyList in an instance.  
  
### `[delete](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/delete)`

|  Deletes a KeyList.  
  
### `[get](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/get)`

|  Gets details of a single KeyList.  
  
### `[list](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/list)`

|  Lists KeyLists in an instance.  
  
### `[removeEntries](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/removeEntries)`

|  Removes entries from a KeyList and returns the updated KeyList.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

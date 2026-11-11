---
url: https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors
title: REST Resource: projects.locations.ullMirroringCollectors \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:45:12.541526+00:00
---

# REST Resource: projects.locations.ullMirroringCollectors  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)
  * [ Reference ](https://docs.cloud.google.com/ull-solution/participants/apis)



Send feedback 

#  REST Resource: projects.locations.ullMirroringCollectors Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: UllMirroringCollector

Message describing UllMirroringCollector object

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "forwardingRule": string,
      "engine": string,
      "state": enum ([State](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors#State)),
      "reconciling": boolean,
      "producerPolicy": enum ([ProducerPolicy](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors#ProducerPolicy))
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The name of the UllMirroringCollector.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`forwardingRule` |  `string` Required. Immutable. The regional load balancer which the mirrored traffic should be forwarded to. Format is: projects/{project}/regions/{region}/forwardingRules/{forwardingRule}  
`engine` |  `string` Required. Immutable. The engine resource to which the collector points to. Format is: projects/{project}/locations/{location}/ullMirroringEngines/{ullMirroringEngine}  
`state` |  `enum (`[State](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors#State)`)` Output only. Current state of the collector.  
`reconciling` |  `boolean` Output only. Whether reconciling is in progress, recommended per <https://google.aip.dev/128>.  
`producerPolicy` |  `enum (`[ProducerPolicy](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors#ProducerPolicy)`)` Output only. Administrative policy set by the service producer.  
  
## State

UllMirroringCollector state. New values may be added to this enum in the future.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`ACTIVE` | Ready.  
`CREATING` | Being created.  
`DELETING` | Being deleted.  
`CLOSED` | Indicates the collector is disabled due to a breaking change in another resource.  
`INACTIVE` | Inactive. Collector is not processing traffic.  
  
## ProducerPolicy

Policy state set administratively by the service producer. New values may be added to this enum in the future.

Enums  
---  
`PRODUCER_POLICY_UNSPECIFIED` | Unspecified policy state.  
`ENABLED` | Normal operational state. Collector is enabled.  
`DISABLED` | Emergency override state. Packet delivery to the Collector is administratively disabled. Used in emergency situations to protect compute and network infrastructure from severe traffic overload.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/create)`

|  Creates a new UllMirroringCollector in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/delete)`

|  Deletes a single UllMirroringCollector.  
  
### `[disable](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/disable)`

|  Disables a single UllMirroringCollector.  
  
### `[enable](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/enable)`

|  Enables a single UllMirroringCollector.  
  
### `[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/get)`

|  Gets details of a single UllMirroringCollector.  
  
### `[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/list)`

|  Lists UllMirroringCollectors in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors/patch)`

|  Updates a single UllMirroringCollector.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

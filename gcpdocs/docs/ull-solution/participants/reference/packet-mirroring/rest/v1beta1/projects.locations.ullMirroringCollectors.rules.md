---
url: https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules
title: REST Resource: projects.locations.ullMirroringCollectors.rules \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:46:45.833058+00:00
---

# REST Resource: projects.locations.ullMirroringCollectors.rules  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)
  * [ Reference ](https://docs.cloud.google.com/ull-solution/participants/apis)



Send feedback 

#  REST Resource: projects.locations.ullMirroringCollectors.rules Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: UllMirroringCollectorRule

UllMirroringCollectorRule is a resource that defines what traffic should be mirrored.

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
      "match": {
        object ([Match](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules#Match))
      },
      "reconciling": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the UllMirroringCollectorRule.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`match` |  `object (`[Match](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules#Match)`)` Required. Match defines what traffic to mirror.  
`reconciling` |  `boolean` Output only. Whether reconciling is in progress, recommended per <https://google.aip.dev/128>.  
  
## Match

Match defines the traffic filtering criteria.

JSON representation  
---  
      
    
    {
      "srcIpRanges": [
        string
      ],
      "dstIpRanges": [
        string
      ],
      "ipProtocols": [
        string
      ],
      "direction": enum ([Direction](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules#Direction)),
      "primaryIpRanges": [
        string
      ]
    }  
  
Fields  
---  
`srcIpRanges[]` |  `string` Optional. Source IP ranges to match. When unset, matches any source IP range.  
`dstIpRanges[]` |  `string` Optional. Destination IP ranges to match. When unset, matches any destination IP range.  
`ipProtocols[]` |  `string` Optional. IP protocols to match. When unset, matches any IP protocol. Examples: "tcp", "udp", "icmp". If unset, matches any IP protocol.  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules#Direction)`)` Optional. Direction of traffic to match. When unset, matches any direction.  
`primaryIpRanges[]` |  `string` Optional. Primary IP ranges to match (for the capture point). When unset, matches any primary IP.  
  
## Direction

Direction defines the direction of traffic. This enum is frozen; no new values will be added.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Not set. Matches any direction.  
`INGRESS` | Traffic inbound to the capture point.  
`EGRESS` | Traffic outbound from the capture point.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/create)`

|  Creates a new UllMirroringCollectorRule for a given UllMirroringCollector.  
  
### `[delete](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/delete)`

|  Deletes a single UllMirroringCollectorRule for a given UllMirroringCollector.  
  
### `[get](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/get)`

|  Gets details of a single UllMirroringCollectorRule.  
  
### `[list](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/list)`

|  Lists UllMirroringCollectorRules for a given UllMirroringCollector.  
  
### `[patch](https://docs.cloud.google.com/ull-solution/participants/reference/packet-mirroring/rest/v1beta1/projects.locations.ullMirroringCollectors.rules/patch)`

|  Updates a single UllMirroringCollectorRule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/BoundaryConfig/
title: BoundaryConfig \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T05:45:24.478777+00:00
---

# BoundaryConfig  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/BoundaryConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  BoundaryConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A BoundaryConfig defines the common configurations regarding Boundaries defined under a parent CRM node (Folder or Organization), such as the partitioning tag key.

JSON representation  
---  
      
    
    {
      "name": string,
      "tagKey": string,
      "etag": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique resource name of the BoundaryConfig. Format: - `organizations/{organization}/boundaryConfig` \- `folders/{folder}/boundaryConfig` Example: `folders/123456789/boundaryConfig`  
`tagKey` |  `string` Optional. The namespaced name of the tag key. Format: `{parent_id}/{tag_key_short_name}` Example: `123456789012/env` (where 123456789012 is the organization ID).  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time this BoundaryConfig was modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo/
title: StorageInfo \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:31.418718+00:00
---

# StorageInfo  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  StorageInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * StorageType



Where a key share is stored.

JSON representation  
---  
      
    
    {
      "storageType": enum ([StorageType](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo#StorageType))
    }  
  
Fields  
---  
`storageType` |  `enum (`[StorageType](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/StorageInfo#StorageType)`)` Required. The kind of environment that stores the key share.  
  
## StorageType

The kind of environment that stores a key share.

Enums  
---  
`STORAGE_TYPE_UNSPECIFIED` | Not specified.  
`GCP_TEE` | A Trusted Execution Environment managed by Google Cloud.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

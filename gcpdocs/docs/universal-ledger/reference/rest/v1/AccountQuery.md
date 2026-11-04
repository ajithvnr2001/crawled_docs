---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AccountQuery/
title: AccountQuery \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:35:53.063876+00:00
---

# AccountQuery  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AccountQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  AccountQuery Stay organized with collections  Save and categorize content based on your preferences. 

A request to query information about an account.

JSON representation  
---  
      
    
    {
      "accountId": string,
      "roundId": string
    }  
  
Fields  
---  
`accountId` |  `string` Required. The ID of the account to get information about.  
`roundId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The ID of the execution round (similar to block "height") at which to request data. The returned account information will be accurate for the world state at this execution round. If unspecified, uses the latest finalized round as known by the serving validator. The state at a given round ID is always consistent and canonical.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 

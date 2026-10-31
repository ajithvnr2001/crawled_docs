---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit/
title: SCMCommit \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:10.589990+00:00
---

# SCMCommit  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  SCMCommit Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



SCMCommit represents commit metadata.

JSON representation  
---  
      
    
    {
      "sha": string,
      "message": string,
      "author": string,
      "authorEmail": string,
      "commitTime": string,
      "url": string
    }  
  
Fields  
---  
`sha` |  `string` Full 40-character SCM commit SHA.  
`message` |  `string` Commit message text.  
`author` |  `string` The author's display name.  
`authorEmail` |  `string` The author's email address.  
`commitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the commit was authored.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`url` |  `string` The SCM provider's HTML URL link for this commit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

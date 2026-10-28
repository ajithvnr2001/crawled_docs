---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo/
title: AuthorizationInfo \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:41.002108+00:00
---

# AuthorizationInfo  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/AuthorizationInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  AuthorizationInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A cryptographic authorization from a user. Used by any API call that needs proof the user approved a specific payload.

JSON representation  
---  
      
    
    {
      "signature": string,
      "signedPayload": string
    }  
  
Fields  
---  
`signature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The signature over `signedPayload`, produced with the user's authorization key.A base64-encoded string.  
`signedPayload` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The exact bytes that were signed. Kept for audit.A base64-encoded string.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

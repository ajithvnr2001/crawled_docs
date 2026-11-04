---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedQueryRequest/
title: SignedQueryRequest \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:35:57.433245+00:00
---

# SignedQueryRequest  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedQueryRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  SignedQueryRequest Stay organized with collections  Save and categorize content based on your preferences. 

A signed query request from the client.

JSON representation  
---  
      
    
    {
      "serializedClientQuery": string,
      "senderSignature": string,
      "senderSigningKeySlot": enum ([KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot))
    }  
  
Fields  
---  
`serializedClientQuery` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. A protobuf serialized `[ClientQuery](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientQuery)` to query the Universal Ledger network.A base64-encoded string.  
`senderSignature` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. The signature of the sender of the query request, computed over the `serializedClientQuery` bytes. If this field is omitted, the query is treated as anonymous, and only public information will be returned.The signature is verified by the server only if the sender identifier is provided in the `[ClientQuery](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientQuery)`. The signature is rejected if expiry time in the serialized `[ClientQuery](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientQuery)` is missing, is in the past, or more than 5 minutes in the future.A base64-encoded string.  
`senderSigningKeySlot` |  `enum (`[KeySlot](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/KeySlot)`)` Optional. The key slot of the sender used to sign the query request. Uses the primary slot of the sender account if not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 

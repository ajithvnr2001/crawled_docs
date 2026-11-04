---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientQuery/
title: ClientQuery \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:30.002337+00:00
---

# ClientQuery  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  ClientQuery Stay organized with collections  Save and categorize content based on your preferences. 

Represents a query request from a client.

JSON representation  
---  
      
    
    {
      "senderId": string,
      "expireTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "accountQuery": {
        object ([AccountQuery](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AccountQuery))
      },
      "transactionStateQuery": {
        object ([TransactionStateQuery](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientQuery#TransactionStateQuery))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`senderId` |  `string` Optional. The sender of the query request.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time at which the query will expire. This helps to limit the exposure to replay attacks. This field is required if the `[SignedQueryRequest](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedQueryRequest)` contains a signature and is optional otherwise. The expiration time must be in the future and at most 5 minutes from the current time, that is `now <= expireTime <= now + 5 min`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
The query request specific message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`accountQuery` |  `object (`[AccountQuery](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/AccountQuery)`)` Optional. Query for the details of an account.  
`transactionStateQuery` |  `object (`[TransactionStateQuery](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/ClientQuery#TransactionStateQuery)`)` Optional. Query for the state of a transaction.  
End of mutually exclusive fields.  
  
## TransactionStateQuery

A request to query the state of a transaction.

JSON representation  
---  
      
    
    {
      "transactionDigestHex": string
    }  
  
Fields  
---  
`transactionDigestHex` |  `string` Required. The transaction ID to get the state of.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 

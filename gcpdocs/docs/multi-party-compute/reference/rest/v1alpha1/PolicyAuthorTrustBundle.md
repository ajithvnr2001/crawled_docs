---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/PolicyAuthorTrustBundle/
title: PolicyAuthorTrustBundle \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:37.843754+00:00
---

# PolicyAuthorTrustBundle  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/PolicyAuthorTrustBundle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  PolicyAuthorTrustBundle Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PolicyAuthor
    * JSON representation



Represents a trusted author list configuration bundle.

JSON representation  
---  
      
    
    {
      "name": string,
      "sequenceNumber": string,
      "authors": [
        {
          object ([PolicyAuthor](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/PolicyAuthorTrustBundle#PolicyAuthor))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the trust bundle. Format: projects/{project}/locations/{location}/instances/{instance}/policyEngine/policyAuthorTrustBundle  
`sequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The sequence number of the bundle for rollback protection.  
`authors[]` |  `object (`[PolicyAuthor](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/PolicyAuthorTrustBundle#PolicyAuthor)`)` Required. The list of authorized policy authors.  
  
## PolicyAuthor

Represents an authorized policy author.

JSON representation  
---  
      
    
    {
      "authorId": string
    }  
  
Fields  
---  
`authorId` |  `string` Required. The policy author's participant ID (e.g. email).  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

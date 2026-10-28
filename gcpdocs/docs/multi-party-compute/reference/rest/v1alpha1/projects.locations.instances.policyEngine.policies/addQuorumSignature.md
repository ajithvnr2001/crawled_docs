---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/addQuorumSignature/
title: Method: projects.locations.instances.policyEngine.policies.addQuorumSignature \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:40.587993+00:00
---

# Method: projects.locations.instances.policyEngine.policies.addQuorumSignature  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies/addQuorumSignature/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.policyEngine.policies.addQuorumSignature Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Custom Method: Appends a software-backed author signature to a policy. Standard UpdatePolicy is explicitly omitted to prevent malicious overwrites.

### HTTP request

`POST https://mpc.googleapis.com/v1alpha1/{name=projects/*/locations/*/instances/*/policyEngine/policies/*}:addQuorumSignature`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the policy to add a signature to. Format: projects/{project}/locations/{location}/instances/{instance}/policyEngine/policies/{policy} It takes the form `projects/{project}/locations/{location}/instances/{instance}/policyEngine/policies/{policies}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "signature": {
        object ([QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature))
      }
    }  
  
Fields  
---  
`signature` |  `object (`[QuorumSignature](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#QuorumSignature)`)` Required. The quorum signature to add.  
  
### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.policyEngine.policies#Policy)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

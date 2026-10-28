---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/list/
title: Method: projects.locations.instances.mpc.keyRings.keys.list \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:35.376487+00:00
---

# Method: projects.locations.instances.mpc.keyRings.keys.list  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.mpc.keyRings.keys.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Keys in a given KeyRing.

### HTTP request

`GET https://mpc.googleapis.com/v1alpha1/{parent=projects/*/locations/*/instances/*/mpc/keyRings/*}/keys`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent key ring resource name. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyRing} It takes the form `projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyring}`.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing Keys.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "keys": [
        {
          object ([Key](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#Key))
        }
      ]
    }  
  
Fields  
---  
`keys[]` |  `object (`[Key](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#Key)`)` The list of keys.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

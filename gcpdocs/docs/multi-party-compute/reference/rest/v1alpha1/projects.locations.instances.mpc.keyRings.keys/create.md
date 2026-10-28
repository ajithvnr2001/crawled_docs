---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/create/
title: Method: projects.locations.instances.mpc.keyRings.keys.create \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:48.833836+00:00
---

# Method: projects.locations.instances.mpc.keyRings.keys.create  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.mpc.keyRings.keys.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Initiates a Distributed Key Generation (DKG) ceremony. This method returns a `[google.longrunning.Operation](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/Operation)` resource, as DKG is an asynchronous operation. See <https://google.aip.dev/151> for more details on LROs.

### HTTP request

`POST https://mpc.googleapis.com/v1alpha1/{parent=projects/*/locations/*/instances/*/mpc/keyRings/*}/keys`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent key ring resource name where the key will be created. Format: projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyRing} It takes the form `projects/{project}/locations/{location}/instances/{instance}/mpc/keyRings/{keyring}`.  
  
### Query parameters

Parameters  
---  
`keyId` |  `string` Required. The ID to use for the key, which will become the final component of the key's resource name.It must be unique within a key ring and match the regular expression `[a-zA-Z0-9_-]{1,63}`.  
  
### Request body

The request body contains an instance of `[Key](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.keyRings.keys#Key)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

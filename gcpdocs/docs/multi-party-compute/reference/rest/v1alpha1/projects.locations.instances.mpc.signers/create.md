---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/create/
title: Method: projects.locations.instances.mpc.signers.create \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:36.105415+00:00
---

# Method: projects.locations.instances.mpc.signers.create  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.mpc.signers.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Registers a new participant entity capable of holding key shares.

### HTTP request

`POST https://mpc.googleapis.com/v1alpha1/{parent=projects/*/locations/*/instances/*}/mpc/signers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent instance resource name where the participant will be created. Format: projects/{project}/locations/{location}/instances/{instance} It takes the form `projects/{project}/locations/{location}/instances/{instance}`.  
  
### Query parameters

Parameters  
---  
`participantId` |  `string` Required. The ID to use for the participant, provided by the client. This ID will become the final component of the participant's resource name.  
  
### Request body

The request body contains an instance of `[Participant](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#Participant)`.

### Response body

If successful, the response body contains a newly created instance of `[Participant](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1alpha1/projects.locations.instances.mpc.signers#Participant)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 

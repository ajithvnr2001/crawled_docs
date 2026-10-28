---
url: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/removeEntries/
title: Method: projects.locations.instances.keyLists.removeEntries \u00a0|\u00a0 Multi-party Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T21:20:44.931208+00:00
---

# Method: projects.locations.instances.keyLists.removeEntries  |  Multi-party Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists/removeEntries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Multi-party Compute ](https://docs.cloud.google.com/multi-party-compute)
  * [ APIs & Reference ](https://docs.cloud.google.com/multi-party-compute/apis)



#  Method: projects.locations.instances.keyLists.removeEntries Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Removes entries from a KeyList and returns the updated KeyList.

Entries not in the KeyList are ignored, so retrying is safe.

### HTTP request

`POST https://mpc.googleapis.com/v1beta/{name=projects/*/locations/*/instances/*/keyLists/*}:removeEntries`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the KeyList to remove entries from. Format: projects/{project}/locations/{location}/instances/{instance}/keyLists/{keyList} It takes the form `projects/{project}/locations/{location}/instances/{instance}/keyLists/{keylist}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entries": [
        {
          object ([Entry](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists#Entry))
        }
      ]
    }  
  
Fields  
---  
`entries[]` |  `object (`[Entry](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists#Entry)`)` Required. The entries to remove. Must contain at least one entry. Entries are matched by `key`, `keyRing`, or `manualEntry.address`; other fields are ignored.  
  
### Response body

If successful, the response body contains an instance of `[KeyList](https://docs.cloud.google.com/multi-party-compute/reference/rest/v1beta/projects.locations.instances.keyLists#KeyList)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

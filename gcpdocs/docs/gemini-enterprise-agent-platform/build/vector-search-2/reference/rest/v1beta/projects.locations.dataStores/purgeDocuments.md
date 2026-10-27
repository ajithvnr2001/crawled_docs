---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/purgeDocuments/
title: Method: projects.locations.dataStores.purgeDocuments \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:37:08.505429+00:00
---

# Method: projects.locations.dataStores.purgeDocuments  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/purgeDocuments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.dataStores.purgeDocuments Stay organized with collections  Save and categorize content based on your preferences. 

Initiates a Long-Running Operation to purge Documents from a DataStore.

`dataStores.purgeDocuments`, `dataStores.importDocuments` and `dataStores.patch` run one at a time per DataStore. While one runs, one more can wait; any further request fails with `ABORTED` until the running operation finishes.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{name}:purgeDocuments`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the DataStore to purge Documents from. Format: `projects/{project}/locations/{location}/dataStores/{dataStore}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "purgeOutputConfig": {
        object ([PurgeOutputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/purgeDocuments#PurgeOutputConfig))
      },
      "force": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`purgeOutputConfig` |  `object (`[PurgeOutputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/purgeDocuments#PurgeOutputConfig)`)` Optional. Configuration of destination for purge documents output.  
`force` |  `boolean` Optional. Actually performs the purge. If `force` is set to `false`, return the expected purge count without deleting any Documents.  
The Documents to purge, given by their Document IDs. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource)`)` Cloud Storage files that list the Documents to purge, one Document ID per line. Each line holds only the ID, not the full resource name. Each URI must name a single file: patterns and folders are not supported.A line that isn't a valid Document ID is reported as an error, and a file with no valid ID fails the purge. An ID that names no Document is skipped, and counted in `ignoredCount` in the operation's metadata. Each file can list at most 100,000 IDs.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/vectorsearch`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## PurgeOutputConfig

Configuration of destination for Purge related output.

JSON representation  
---  
      
    
    {
      "errorGcsPrefix": string
    }  
  
Fields  
---  
`errorGcsPrefix` |  `string` Optional. Cloud Storage prefix for purge errors. The prefix must not contain any objects. Purge errors will be written to sharded files under this prefix, one per line, as a JSON-encoded `google.rpc.Status` message.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

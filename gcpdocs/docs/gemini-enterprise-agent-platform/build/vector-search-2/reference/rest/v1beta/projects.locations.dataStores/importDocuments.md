---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/importDocuments/
title: Method: projects.locations.dataStores.importDocuments \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:37:41.176820+00:00
---

# Method: projects.locations.dataStores.importDocuments  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/importDocuments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.dataStores.importDocuments Stay organized with collections  Save and categorize content based on your preferences. 

Initiates a Long-Running Operation to import Documents into a DataStore.

A file that was already imported successfully is skipped unless its Cloud Storage object has been overwritten since or, for `SOURCE_FORMAT_DOCUMENT_JSON`, its metadata has changed. Files that failed in an earlier import are processed again. Individual files that can't be imported are reported in the error report (see `ImportOutputConfig.error_gcs_prefix`) rather than failing the whole import.

`dataStores.importDocuments`, `dataStores.purgeDocuments` and `dataStores.patch` run one at a time per DataStore. While one runs, one more can wait; any further request fails with `ABORTED` until the running operation finishes. To import many files, list them all in `inputUris` of one request rather than sending parallel requests.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{name}:importDocuments`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the DataStore to import Documents into. Format: `projects/{project}/locations/{location}/dataStores/{dataStore}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "importOutputConfig": {
        object ([ImportOutputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/importDocuments#ImportOutputConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`importOutputConfig` |  `object (`[ImportOutputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores/importDocuments#ImportOutputConfig)`)` Optional. Configuration of destination for import documents output: where to write the import's error report.  
Required. The source of the input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource)`)` Cloud Storage location for the input content. With the default `sourceFormat`, a URI can be a pattern such as `gs://my-bucket/folder/*`, which matches the objects directly in `folder` but not those in its subfolders. One import can include at most 100,000 files for an `UNSTRUCTURED` DataStore, or 100 for a `VIDEO` DataStore.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/vectorsearch`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ImportOutputConfig

Configuration of destination for import documents related output.

JSON representation  
---  
      
    
    {
      "errorGcsPrefix": string
    }  
  
Fields  
---  
`errorGcsPrefix` |  `string` Optional. URI prefix of the Cloud Storage location to write any errors encountered during the import. The prefix must not contain any objects. Errors are written to sharded files under this prefix, one per line, as a JSON-encoded `google.rpc.Status` message. If this field is empty, no error report is written.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

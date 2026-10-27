---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents
title: REST Resource: projects.locations.dataStores.documents \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:37:57.854395+00:00
---

# REST Resource: projects.locations.dataStores.documents  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.dataStores.documents Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Document

A Document is a single unit of content ingested into a DataStore. It is a sub-resource of a DataStore. During ingestion a Document is parsed and chunked into one or more Segments.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "content": {
        object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents#Content))
      },
      "etag": string,
      "metadata": {
        object ([DocumentMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents#DocumentMetadata))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The fully qualified resource name of the Document.Format: `projects/{project}/locations/{location}/dataStores/{dataStoreId}/documents/{documentId}` The documentId must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).When ImportDocuments imports files directly (the default source format), the service derives the documentId from the file's Cloud Storage URI: re-importing the same URI updates the same Document, and a renamed or moved file becomes a new Document. With `SOURCE_FORMAT_DOCUMENT_JSON`, the documentId is taken from the `name` given in the input file.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the Document was created at.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the Document was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`content` |  `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents#Content)`)` Optional. The unstructured data linked to this Document: the Cloud Storage file it was imported from. Required in each line of a `SOURCE_FORMAT_DOCUMENT_JSON` input file.  
`etag` |  `string` Optional. The etag of the Document.  
`metadata` |  `object (`[DocumentMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents#DocumentMetadata)`)` Optional. User-defined metadata for this Document. The metadata values must conform to the `documentMetadataSchema` defined on the parent DataStore.  
  
## Content

Unstructured data linked to this Document.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsUri": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The content of the unstructured Document. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsUri` |  `string` The Cloud Storage URI of the content. Only Cloud Storage URIs (e.g. `gs://bucket-name/path/to/file`) are supported.  
End of mutually exclusive fields.  
  
## DocumentMetadata

User-defined metadata associated with a Document.

JSON representation  
---  
      
    
    {
      "value": {
        object
      }
    }  
  
Fields  
---  
`value` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The metadata value, as a JSON object. The value must conform to the `documentMetadataSchema` defined on the parent DataStore.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents/get)`

|  Gets a Document.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents/list)`

|  Lists Documents in a DataStore.  
  
### `[search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.dataStores.documents/search)`

|  Searches the Documents of a single DataStore.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

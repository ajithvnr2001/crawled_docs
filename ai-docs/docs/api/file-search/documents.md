---
url: https://ai.google.dev/api/file-search/documents/
title: Documents \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:15:53.672345+00:00
---

# Documents  |  Gemini API  |  Google AI for Developers

> Source: https://ai.google.dev/api/file-search/documents/

Gemini 4 Argon is now available. [Try it out](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon). 

  * [ Home ](https://ai.google.dev/)
  * [ Gemini API ](https://ai.google.dev/gemini-api)
  * [ API reference ](https://ai.google.dev/api)



Send feedback 

#  Documents

The File Search API references your raw source files, or documents, as temporary File objects.

## Method: fileSearchStores.documents.delete

  * Endpoint
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Deletes a `Document`.

### Endpoint

delete  `https://generativelanguage.googleapis.com/v1beta/{name=fileSearchStores/*/documents/*}`   


### Path parameters

`name` `string` Required. The resource name of the `Document` to delete. Example: `fileSearchStores/my-file-search-store-123/documents/the-doc-abc` It takes the form `fileSearchStores/{filesearchstore}/documents/{document}`.

### Query parameters

| `force` `boolean` Optional. If set to true, any `Chunk`s and objects related to this `Document` will also be deleted.If false (the default), a `FAILED_PRECONDITION` error will be returned if `Document` contains any `Chunk`s.

### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

## Method: fileSearchStores.documents.get

  * Endpoint
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes

Gets information about a specific `Document`.

### Endpoint

get  `https://generativelanguage.googleapis.com/v1beta/{name=fileSearchStores/*/documents/*}`   


### Path parameters

| `name` `string` Required. The name of the `Document` to retrieve. Example: `fileSearchStores/my-file-search-store-123/documents/the-doc-abc` It takes the form `fileSearchStores/{filesearchstore}/documents/{document}`.

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Document](https://ai.google.dev/api/file-search/documents#Document)`.

## Method: fileSearchStores.documents.list

  * Endpoint
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes

Lists all `Document`s in a `Corpus`.

### Endpoint

get  `https://generativelanguage.googleapis.com/v1beta/{parent=fileSearchStores/*}/documents`   


### Path parameters

| `parent` `string` Required. The name of the `FileSearchStore` containing `Document`s. Example: `fileSearchStores/my-file-search-store-123` It takes the form `fileSearchStores/{filesearchstore}`.

### Query parameters

| `pageSize` `integer` Optional. The maximum number of `Document`s to return (per page). The service may return fewer `Document`s.If unspecified, at most 10 `Document`s will be returned. The maximum size limit is 20 `Document`s per page. | `pageToken` `string` Optional. A page token, received from a previous `documents.list` call.Provide the `nextPageToken` returned in the response as an argument to the next request to retrieve the next page.When paginating, all other parameters provided to `documents.list` must match the call that provided the page token.

### Request body

The request body must be empty.

### Response body

Response from `documents.list` containing a paginated list of `Document`s. The `Document`s are sorted by ascending `document.create_time`. If successful, the response body contains data with the following structure: | Fields  
  
`documents[]` `object (`[Document](https://ai.google.dev/api/file-search/documents#Document)`)` The returned `Document`s. | `nextPageToken` `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no more pages. | JSON representation  
---  
      
    
    {
      "documents": [
        {
          object ([Document](https://ai.google.dev/api/file-search/documents#Document))
        }
      ],
      "nextPageToken": string
    }  
  
## REST Resource: fileSearchStores.documents

  * Resource: Document
    * JSON representation
  * CustomMetadata
    * JSON representation
  * StringList
    * JSON representation
  * State
  * Methods



## Resource: Document

A `Document` is a collection of `Chunk`s.

Fields  
  
`name` `string` Immutable. Identifier. The `Document` resource name. The ID (name excluding the "fileSearchStores/*/documents/" prefix) can contain up to 40 characters that are lowercase alphanumeric or dashes (-). The ID cannot start or end with a dash. If the name is empty on create, a unique name will be derived from `displayName` along with a 12 character random suffix. Example: `fileSearchStores/{file_search_store_id}/documents/my-awesome-doc-123a456b789c` | `displayName` `string` Optional. The human-readable display name for the `Document`. The display name must be no more than 512 characters in length, including spaces. Example: "Semantic Retriever Documentation" | `customMetadata[]` `object (`[CustomMetadata](https://ai.google.dev/api/file-search/documents#CustomMetadata)`)` Optional. User provided custom metadata stored as key-value pairs used for querying. A `Document` can have a maximum of 20 `CustomMetadata`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The Timestamp of when the `Document` was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The Timestamp of when the `Document` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `state` `enum (`[State](https://ai.google.dev/api/file-search/documents#State)`)` Output only. Current state of the `Document`. | `sizeBytes` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The size of raw bytes ingested into the Document. | `mimeType` `string` Output only. The mime type of the Document. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "customMetadata": [
        {
          object ([CustomMetadata](https://ai.google.dev/api/file-search/documents#CustomMetadata))
        }
      ],
      "updateTime": string,
      "createTime": string,
      "state": enum ([State](https://ai.google.dev/api/file-search/documents#State)),
      "sizeBytes": string,
      "mimeType": string
    }  
  
## CustomMetadata

User provided metadata stored as key-value pairs.

Fields  
  
`key` `string` Required. The key of the metadata to store. | `value` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`stringValue` `string` The string value of the metadata to store. | `stringListValue` `object (`[StringList](https://ai.google.dev/api/file-search/documents#StringList)`)` The StringList value of the metadata to store. | `numericValue` `number` The numeric value of the metadata to store. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "key": string,
    
      // value
      "stringValue": string,
      "stringListValue": {
        object ([StringList](https://ai.google.dev/api/file-search/documents#StringList))
      },
      "numericValue": number
      // Union type
    }  
  
## StringList

User provided string values assigned to a single metadata key.

Fields  
  
`values[]` `string` The string values of the metadata to store. | JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
## State

States for the lifecycle of a `Document`.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`STATE_PENDING` | Some `Chunks` of the `Document` are being processed (embedding and vector storage).  
`STATE_ACTIVE` | All `Chunks` of the `Document` is processed and available for querying.  
`STATE_FAILED` | Some `Chunks` of the `Document` failed processing.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-28 UTC."],[],[]] 

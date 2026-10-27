---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource/
title: GcsSource \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T05:36:54.744171+00:00
---

# GcsSource  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  GcsSource Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage location for the input content.

JSON representation  
---  
      
    
    {
      "inputUris": [
        string
      ],
      "sourceFormat": enum ([SourceFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource#SourceFormat))
    }  
  
Fields  
---  
`inputUris[]` |  `string` Required. Cloud Storage URIs to input files. How the URIs are read depends on the method: see `ImportDocumentsRequest.gcs_source` and `PurgeDocumentsRequest.gcs_source`.The whole request, including every URI, must not exceed 2,000,000 bytes. Split a larger set of URIs across multiple requests.  
`sourceFormat` |  `enum (`[SourceFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/GcsSource#SourceFormat)`)` Optional. Format of the input files. Used by ImportDocuments; PurgeDocuments ignores it.  
  
## SourceFormat

SourceFormat specifies the format of the input content. This enum can be used in GcsSource to notify the service how to parse the input URIs.

Enums  
---  
`SOURCE_FORMAT_UNSPECIFIED` | Default value. Each input URI names a file to import, or a pattern that matches files to import (see `ImportDocumentsRequest.gcs_source`). Each file is imported as a separate Document.An `UNSTRUCTURED` DataStore accepts PDF (`.pdf`), plain text (`.txt`), Word (`.docx`), PowerPoint (`.pptx`) and Excel (`.xlsx`, `.xlsm`) files of up to 200 MB (200,000,000 bytes). A `VIDEO` DataStore accepts video files of up to 600 GB that the service can decode and that are at most 15 hours long. A file that doesn't meet these requirements is reported in the error report rather than failing the import.  
`SOURCE_FORMAT_DOCUMENT_JSON` | Each input URI names a JSON Lines file: one Document per line, in the JSON format of the Document resource. Each line must set `name`, which gives the Document ID, and `content.gcs_uri`, and can set `metadata`, which must conform to the DataStore's `documentMetadataSchema`. Patterns are not supported in the input URIs.The files that the lines reference must meet the same requirements as for `SOURCE_FORMAT_UNSPECIFIED`. Lines that can't be parsed or that don't conform are reported in the error report and skipped.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

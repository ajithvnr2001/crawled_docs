---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchFileBlame/
title: Method: projects.locations.connections.gitRepositoryLinks.fetchFileBlame \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:08.033695+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.fetchFileBlame  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchFileBlame/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.fetchFileBlame Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * BlameRange
    * JSON representation
  * Try it!



Fetches blame information for a file or line range in a file.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchFileBlame`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the GitRepositoryLink in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Query parameters

Parameters  
---  
`ref` |  `string` Required. The SCM commit SHA, or symbolic revision (for example, branch name, tag) from which to fetch the blame.  
`path` |  `string` Required. The file path within the repository.  
`firstLine` |  `integer` Optional. The 1-indexed starting line number of the range to blame (inclusive). If not specified, blame begins at line 1.  
`lastLine` |  `integer` Optional. The 1-indexed ending line number of the range to blame (inclusive). If not specified, blame extends to the end of the file.  
  
### Request body

The request body must be empty.

### Response body

Response message for gitRepositoryLinks.fetchFileBlame.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ranges": [
        {
          object ([BlameRange](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchFileBlame#BlameRange))
        }
      ]
    }  
  
Fields  
---  
`ranges[]` |  `object (`[BlameRange](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchFileBlame#BlameRange)`)` The list of blame ranges for the file.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `developerconnect.gitRepositoryLinks.fetchFileBlame`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## BlameRange

BlameRange represents blame information for a range of lines.

JSON representation  
---  
      
    
    {
      "firstLine": integer,
      "lastLine": integer,
      "commit": {
        object ([SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit))
      }
    }  
  
Fields  
---  
`firstLine` |  `integer` The 1-indexed starting line number of the range (inclusive).  
`lastLine` |  `integer` The 1-indexed ending line number of the range (inclusive).  
`commit` |  `object (`[SCMCommit](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/SCMCommit)`)` The commit metadata for this line range.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

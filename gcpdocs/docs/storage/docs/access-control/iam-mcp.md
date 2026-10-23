---
url: https://docs.cloud.google.com/storage/docs/access-control/iam-mcp/
title: IAM permissions for Cloud Storage MCP server methods \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:50:45.549238+00:00
---

# IAM permissions for Cloud Storage MCP server methods  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/iam-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IAM permissions for Cloud Storage MCP server methods Stay organized with collections  Save and categorize content based on your preferences. 

To run Cloud Storage [MCP server methods](https://docs.cloud.google.com/storage/docs/use-cloud-storage-mcp), you need access to the target Cloud Storage resources. You manage access control by granting Identity and Access Management (IAM) roles to principals, such as users, groups, and service accounts. Each role contains a set of permissions. If you want to create custom roles with specific permissions, this document lists the permissions that are required for each MCP server method.

Method | Required IAM Permissions  
---|---  
`create_bucket` | `mcp.tools.call`  
`storage.buckets.create`  
`delete_bucket` | `mcp.tools.call`  
`storage.buckets.delete`  
`delete_object` | `mcp.tools.call`  
`storage.objects.delete`  
`get_object_metadata` | `mcp.tools.call`  
`storage.objects.get`  
`list_buckets` | `mcp.tools.call`  
`storage.buckets.list`  
`list_objects` | `mcp.tools.call`  
`storage.objects.list`  
`read_object` | `mcp.tools.call`  
`storage.objects.get`  
`write_text` | `mcp.tools.call`  
`storage.objects.create`  
  
## What's next

  * Learn about [IAM for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam).

  * For a list of predefined roles and the permissions that they contain, see [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

  * [Grant IAM roles](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) at the project and bucket level.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 

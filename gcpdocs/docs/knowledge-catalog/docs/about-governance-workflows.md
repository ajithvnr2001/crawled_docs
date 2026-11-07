---
url: https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows/
title: About governance workflows \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-07T05:43:20.099689+00:00
---

# About governance workflows  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About governance workflows Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Requesting single metadata changes to business glossaries and entries is available in private preview. To request access to this feature, fill in the [access form](https://forms.gle/eFMGqsaKTUJ62mrR7). 

Governance workflows let you set up automated controls and approval mechanisms for organizational data resources. With these workflows, you can help ensure that authorized individuals or teams manage access to your data products and curate catalog and glossary metadata.

Using governance workflows has the following benefits:

  * Data consumers can find relevant data products and request access directly within Knowledge Catalog (formerly Dataplex Universal Catalog), replacing manual support ticketing processes.
  * Upon request approval, the system automatically grants the required Identity and Access Management (IAM) roles and group memberships, eliminating manual administrative overhead and reducing time-to-access.
  * System logs capture audit trails of requests, justifications, approver decisions, and timestamps to support compliance auditing.
  * Centralized approval mechanisms for sensitive data assets help ensure that access and metadata updates are restricted to authorized users and teams.



## Use cases

Governance workflows support automated access management and metadata curation across various scenarios:

  * **Data product access management** : a marketing manager or risk analyst requests access to a curated sales or transaction history data product to analyze customer behavior or build risk models. Upon approval, the required IAM roles are automatically provisioned.
  * **Business glossary curation** : an organization delegates creating and updating business glossary categories and terms to domain contributors or external contractors. Contractors submit governance requests for review by central data stewards before updating the glossary.
  * **Catalog entry and batch metadata enrichment** : data contributors or automated enrichment agents propose single or batch updates to catalog entries, such as creating custom entries, updating descriptions and aspects, or linking entries to business glossary terms. Data owners can review and approve the changes in a single workflow.



## Use governance workflows in Knowledge Catalog

You can use governance workflows to request access to data products, request single-resource metadata changes to business glossaries and Knowledge Catalog entries, and request batch metadata changes for entries and entry links.

### Concurrency

Multiple pending metadata change requests can coexist on a single resource. Knowledge Catalog uses a _last writer wins_ model, which means the most recently approved change overwrites prior updates, regardless of when requests were submitted. Pending requests remain valid even if the resource is updated directly or by another approved request.

### Supported metadata operations

The following table lists the resources and operations supported by metadata change requests:

Resource | Create | Update | Delete  
---|---|---|---  
**Glossary category** | Yes | Yes | Yes  
**Glossary term** | Yes | Yes | Yes  
**Entry** | Yes | Yes | Yes  
**Entry link** | Yes | No | Yes  
  
## Batch metadata change requests

You can use the Dataplex API to group metadata operations into a single change request.

### Supported batch metadata operations

The following table lists the resources and operations supported by batch metadata change requests:

Resource | Create | Update | Delete  
---|---|---|---  
**Entry** | Yes | Yes | Yes  
**Entry link** | Yes | Yes | Yes  
  
A batch metadata change request can originate in the following ways:

  * **Submitted directly by a user** : you send a REST API request to create a batch change request for entries and entry links.
  * **Generated automatically by the enrichment agent** : when an enrichment agent run generates metadata recommendations that require human review instead of auto-publishing, the agent creates a batch change request.



## Governance workflows processing path

Knowledge Catalog tracks requests throughout their lifecycle using status values. The following table describes each status for single and batch change requests:

Status | Single requests | Batch metadata change requests  
---|---|---  
`NEW` | Pending review. Only the author can edit the request, and only the author or a workflow administrator can delete it. | Pending review. The author can edit user-submitted requests, reviewers can edit enrichment agent requests, and the author or a workflow administrator can delete the request.  
`APPLYING` | Not applicable. | Approved and being applied in the background.  
`APPROVED` | Approved and applied. | Approved, and at least one change in the batch succeeded. Any item-level errors are listed in the response.  
`FAILED` | Couldn't be applied. Updating the request resets its status to `NEW` for re-approval. | None of the changes in the batch could be applied. Updating the request resets its status to `NEW` for re-approval.  
`REJECTED` | Declined by an approver. No changes were applied. | Declined by an approver. No changes were applied.  
  
When a request is manually deleted, its target resource is deleted, or it expires after 90 days, Knowledge Catalog permanently removes the request from storage. Subsequent queries for the request return a `404 NOT_FOUND` error.

## Governance workflows roles

Governance workflows roles include requesters, approvers, and workflow administrators. The following table describes the roles in detail:

Role | Description  
---|---  
**Requester** | Creates and submits requests, and can edit or delete their own requests while in the `NEW` state.  
**Approver** | Reviews, approves, or rejects requests. For batch metadata change requests generated by the enrichment agent, approvers can also edit the proposed batch changes before approving.  
**Workflow administrator** | Monitors compliance, configures workflow policies, and maintains the request backlog. Administrators can view audit trails across all request states and have administrative deletion permissions to remove requests in any state.  
  
## Limitations

  * Governance workflows aren't supported for [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) projects.
  * Governance workflows don't support [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/knowledge-catalog/docs/cmek).
  * Governance workflows don't support [VPC Service Controls](https://docs.cloud.google.com/knowledge-catalog/docs/vpc-sc).



## What's next

  * Learn how to [request single-resource metadata changes](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-workflows).
  * Learn how to [request batch metadata changes](https://docs.cloud.google.com/knowledge-catalog/docs/request-batch-metadata-changes).
  * Learn how to [manage requests](https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests).
  * Learn how to [request access to data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#request-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-07 UTC."],[],[]] 

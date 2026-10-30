---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.menuIssueClusters
title: REST Resource: projects.locations.brands.menuIssueClusters \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:42.153110+00:00
---

# REST Resource: projects.locations.brands.menuIssueClusters  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.menuIssueClusters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  REST Resource: projects.locations.brands.menuIssueClusters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MenuIssueCluster
    * JSON representation
  * ClusteredEntityIssue
    * JSON representation
  * Methods



## Resource: MenuIssueCluster

Represents a brand-level root-cause cluster of menu issues aggregated across one or more stores.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "description": string,
      "actionPlan": string,
      "issueCategories": [
        string
      ],
      "entityTypes": [
        enum ([EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/EntityType))
      ],
      "affectedStoreCount": integer,
      "affectedEntityCount": integer,
      "totalIssueCount": integer,
      "entityIssues": [
        {
          object ([ClusteredEntityIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.menuIssueClusters#ClusteredEntityIssue))
        }
      ],
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the menu issue cluster. Format: projects/{project}/locations/{location}/brands/{brand}/menuIssueClusters/{menu_issue_cluster}  
`title` |  `string` Output only. A concise, human-readable title summarizing the shared root cause of the cluster.  
`description` |  `string` Output only. A detailed explanation of the shared root cause across all issues in the cluster.  
`actionPlan` |  `string` Output only. A free-text summary of the recommended operator action plan to resolve the shared root cause. Entity-specific remediation actions are available on `entityIssues`.  
`issueCategories[]` |  `string` Output only. Issue categories present in this cluster (e.g. MISSING_CATEGORY, MODIFIER_AS_PRIMARY_ITEM).  
`entityTypes[]` |  `enum (`[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/EntityType)`)` Output only. Entity types present in this cluster.  
`affectedStoreCount` |  `integer` Output only. The number of stores in the brand affected by this cluster.  
`affectedEntityCount` |  `integer` Output only. The number of unique menu entities affected in this cluster.  
`totalIssueCount` |  `integer` Output only. The total number of store-level menu issues grouped into this cluster.  
`entityIssues[]` |  `object (`[ClusteredEntityIssue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.menuIssueClusters#ClusteredEntityIssue)`)` Output only. The entity issues in this cluster, each with its own remediation actions. Only returned in MENU_ISSUE_CLUSTER_VIEW_FULL.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this cluster was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ClusteredEntityIssue

Represents a deduplicated menu entity issue within a brand-level MenuIssueCluster, aggregated across all stores where the entity exhibits the issue.

JSON representation  
---  
      
    
    {
      "entityId": string,
      "entityDisplayName": string,
      "entityType": enum ([EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/EntityType)),
      "issueCategory": string,
      "explanation": string,
      "confidenceLevel": enum ([ConfidenceLevel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ConfidenceLevel)),
      "suggestedRemediationActions": [
        {
          object ([RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/RemediationAction))
        }
      ],
      "affectedStoreCount": integer
    }  
  
Fields  
---  
`entityId` |  `string` Output only. The ID of the affected menu entity.  
`entityDisplayName` |  `string` Output only. Human-readable display name of the affected entity.  
`entityType` |  `enum (`[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/EntityType)`)` Output only. The type of the affected entity.  
`issueCategory` |  `string` Output only. The category of the issue flagged on this entity.  
`explanation` |  `string` Output only. A representative explanation of why the issue was flagged on this entity.  
`confidenceLevel` |  `enum (`[ConfidenceLevel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ConfidenceLevel)`)` Output only. The highest confidence level observed for this entity issue across stores.  
`suggestedRemediationActions[]` |  `object (`[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/RemediationAction)`)` Output only. Entity-specific remediation actions recommended to fix this issue (including entity-specific rename or category payloads).  
`affectedStoreCount` |  `integer` Output only. The number of stores where this entity issue was detected.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.menuIssueClusters/get)`

|  Gets a menu issue cluster.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands.menuIssueClusters/list)`

|  Lists menu issue clusters for a brand.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

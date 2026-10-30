---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues
title: REST Resource: projects.locations.menus.issues \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:40:29.296806+00:00
---

# REST Resource: projects.locations.menus.issues  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  REST Resource: projects.locations.menus.issues Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MenuIssue
    * JSON representation
  * State
  * AuditLogEntry
    * JSON representation
  * Methods



## Resource: MenuIssue

Represents a detected problem in a menu during an audit.

JSON representation  
---  
      
    
    {
      "name": string,
      "entityId": string,
      "entityDisplayName": string,
      "entityType": enum ([EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EntityType)),
      "issueCategory": string,
      "explanation": string,
      "confidenceLevel": enum ([ConfidenceLevel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ConfidenceLevel)),
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues#State)),
      "suggestedRemediationActions": [
        {
          object ([RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction))
        }
      ],
      "firstDetectTime": string,
      "lastDetectTime": string,
      "resolveTime": string,
      "regressionCount": integer,
      "auditLogEntries": [
        {
          object ([AuditLogEntry](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues#AuditLogEntry))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the MenuIssue. Format: projects/{project}/locations/{location}/menus/{menu}/issues/{issue}  
`entityId` |  `string` Output only. The ID of the affected entity.  
`entityDisplayName` |  `string` Output only. Human-readable name of the affected entity to simplify UI rendering.  
`entityType` |  `enum (`[EntityType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/EntityType)`)` Output only. The type of the affected entity.  
`issueCategory` |  `string` Output only. The category of the issue (e.g. STRANGE_ITEM etc).  
`explanation` |  `string` Output only. A detailed explanation of why the issue was flagged.  
`confidenceLevel` |  `enum (`[ConfidenceLevel](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/ConfidenceLevel)`)` Output only. The confidence level of the detected issue.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues#State)`)` Output only. The current resolution state of the issue.  
`suggestedRemediationActions[]` |  `object (`[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction)`)` Output only. Actions recommended to fix the issue.  
`firstDetectTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the issue was first detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastDetectTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the issue was most recently detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resolveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the issue was resolved.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`regressionCount` |  `integer` Output only. The number of times this issue has regressed after resolution.  
`auditLogEntries[]` |  `object (`[AuditLogEntry](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues#AuditLogEntry)`)` Output only. The audit trail of actions taken on this issue.  
  
## State

The current resolution state of the issue.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified issue state.  
`OPEN` | The issue is active and requires triage.  
`AUTO_RESOLVED` | The issue was resolved automatically by the system due to high confidence.  
`MANUALLY_RESOLVED` | The issue was manually reviewed and resolved by a human operator.  
`CLOSED_WONT_FIX` | The issue was intentionally ignored and should not trigger alerts.  
`REGRESSED` | The issue reappeared in the menu data after being previously resolved.  
  
## AuditLogEntry

Represents a single historical action taken on an issue.

JSON representation  
---  
      
    
    {
      "user": string,
      "recordTime": string,
      "appliedRemediationAction": {
        object ([RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction))
      },
      "resultingState": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues#State))
    }  
  
Fields  
---  
`user` |  `string` Output only. The email address of the user or principal who performed the action.  
`recordTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the action was recorded.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`appliedRemediationAction` |  `object (`[RemediationAction](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/RemediationAction)`)` Output only. The remediation action that was applied, if any.  
`resultingState` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues#State)`)` Output only. The state of the issue after the action was applied.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues/get)`

|  Gets a menu issue.  
  
### `[ignore](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues/ignore)`

|  Ignores a menu issue, marking it as CLOSED_WONT_FIX.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues/list)`

|  Lists menu issues.  
  
### `[resolve](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1beta/projects.locations.menus.issues/resolve)`

|  Resolves a menu issue and records the remediation action taken.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

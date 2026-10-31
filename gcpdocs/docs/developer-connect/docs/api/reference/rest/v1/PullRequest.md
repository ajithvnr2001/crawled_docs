---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest/
title: PullRequest \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:10.031003+00:00
---

# PullRequest  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  PullRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * State
  * Mergeability



Message representing a SCM Pull Request.

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
      "body": string,
      "headRef": string,
      "baseRef": string,
      "author": string,
      "createTime": string,
      "updateTime": string,
      "mergeTime": string,
      "closeTime": string,
      "declineTime": string,
      "state": enum ([State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest#State)),
      "mergeability": enum ([Mergeability](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest#Mergeability)),
      "htmlUrl": string
    }  
  
Fields  
---  
`id` |  `string` Required. The ID of the PR.  
`title` |  `string` Required. The title of the PR.  
`body` |  `string` Optional. The body description of the PR.  
`headRef` |  `string` Required. The source commit SHA of the head branch.  
`baseRef` |  `string` Required. The target commit SHA of the base branch.  
`author` |  `string` Output only. The username of the author.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mergeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was merged.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`closeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was closed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`declineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the PR was declined. Only set for SCM providers that support declining pull requests. Never set for GitHub, GitHub Enterprise, GitLab, or GitLab Enterprise, where a pull request closed without being merged is `CLOSED`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest#State)`)` Output only. The current state of the PR.  
`mergeability` |  `enum (`[Mergeability](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/PullRequest#Mergeability)`)` Output only. The mergeability state of the pull request.  
`htmlUrl` |  `string` Output only. The HTML URL of the pull request on the SCM provider.  
  
## State

The state of the PR.

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`OPEN` | The PR is open.  
`CLOSED` | The PR is closed.  
`MERGED` | The PR is merged.  
`DECLINED` | The PR is declined. Only used by SCM providers that support declining pull requests. Never used for GitHub, GitHub Enterprise, GitLab, or GitLab Enterprise, where a pull request closed without being merged is `CLOSED`.  
  
## Mergeability

The mergeability state of a pull request.

Enums  
---  
`MERGEABILITY_UNSPECIFIED` | Mergeability state is unspecified.  
`MERGEABLE` | The pull request can be merged cleanly without Git conflicts.  
`CONFLICTING` | The pull request has merge conflicts and cannot be merged cleanly.  
`COMPUTING` | The mergeability state is currently being computed asynchronously by the upstream SCM provider.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

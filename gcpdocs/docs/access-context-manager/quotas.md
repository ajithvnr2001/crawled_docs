---
url: https://docs.cloud.google.com/access-context-manager/quotas/
title: Quotas and limits \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:37:41.877895+00:00
---

# Quotas and limits  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/access-context-manager/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Access Context Manager. Quotas and limits specified in this document are subject to change.

Access Context Manager quota enforcement is integrated with [Cloud Quotas](https://docs.cloud.google.com/docs/quotas/overview), allowing administrators to view system limits and current utilization.

For quotas and limits for service perimeters, a component of VPC Service Controls, see [VPC Service Controls quotas and limits](https://docs.cloud.google.com/vpc-service-controls/quotas).

## View quotas in the Google Cloud console

You can view organization-level Access Context Manager quotas and limits in the centralized **Quotas & System Limits** page in the Google Cloud console:

  1. In the Google Cloud console, go to the **Quotas & System Limits** page.

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas?service=accesscontextmanager.googleapis.com)

  2. In the resource selector, select your organization.

  3. To inspect effective limits and current utilization, filter by service name `accesscontextmanager.googleapis.com`.




You can also query quota metrics programmatically using the [Cloud Quotas API](https://docs.cloud.google.com/docs/quotas/reference/rest).

## Request rate limits

Access Context Manager enforces the following API request rate limits:

Request type | Limit | Scope  
---|---|---  
Read requests | 500 requests per minute | Per organization  
Write requests | 50 requests per minute | Per organization  
  
A read request is an operation that retrieves Access Context Manager resources, such as getting or listing access levels or access policies. A write request is an operation that creates, updates, replaces, or deletes an Access Context Manager resource.

## Access policy limits

The following limits apply to access policies and access levels within an organization:

Resource type | Limit | Scope | Notes  
---|---|---|---  
Organization-level access policy | 1 | Per organization | Only one organization-level access policy can exist per organization.  
Folder and project-scoped access policies | 50 | Per organization | Applies across all scoped policies within the organization.  
Access levels | 500 | Per access policy | Applies cumulatively across all basic and custom access levels in a policy.  
Conditions per access level | 40 | Per basic access level | Maximum number of conditions configured in a single basic access level.  
List items per condition attribute | 200 | Per condition attribute | For example, the number of IP subnetwork CIDR ranges in a single condition.  
VPC networks | 500 | Per access policy | Count of VPC networks referenced across all access levels in a policy.  
  
## Custom access level limits

The following limits apply specifically to [custom access levels](https://docs.cloud.google.com/access-context-manager/docs/custom-access-levels) using Common Expression Language (CEL):

Constraint | Limit | Notes  
---|---|---  
Maximum elements in list | 200 | The maximum number of list elements in a CEL expression—for example, in list literals or helper function arguments.  
Maximum CEL expression string length | 100 | Maximum character length for string literals in CEL expressions.  
Maximum CEL expression depth | 20 | Maximum syntax tree nesting depth of a CEL expression.  
Maximum AST node count | 4,000 | Maximum number of abstract syntax tree (AST) nodes allowed in a compiled CEL expression.  
  
## Request quota increases

Only the **Folder and project-scoped access policies** quota per organization is eligible for an increase. All other quotas and system limits specified on this page are fixed platform constraints designed to ensure system scalability and availability.

To request an increase for scoped access policies, do the following:

  1. Check your current quota usage in the Google Cloud console and confirm that your organization is close to the 50-policy limit.
  2. Create a case with [Google Cloud Support](https://cloud.google.com/support).

**Note:** Requesting a quota increase directly through the **Quotas & System Limits** page in the Google Cloud console does not automatically open a support case. You must manually submit a support case.
  3. Provide a clear business justification. Valid justifications include that it's required for organization growth or for policy segmentation.




Requests generally take 2 to 3 weeks to process and require manual review and approval by Google Cloud Support and engineering teams.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

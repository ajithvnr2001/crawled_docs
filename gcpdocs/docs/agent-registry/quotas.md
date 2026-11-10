---
url: https://docs.cloud.google.com/agent-registry/quotas/
title: Quotas and system limits \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T16:58:24.369627+00:00
---

# Quotas and system limits  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Resources ](https://docs.cloud.google.com/agent-registry/resources)



Send feedback 

#  Quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry uses quotas and system limits to maintain fair resource allocation, prevent service overloads, and help you manage resource use.

Quotas and system limits are similar but differ in the following ways:

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help maintain fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

## Allocation quotas

Allocation quotas restrict the amount of a specific resource that Agent Registry lets you use at a given time. When you create a resource, your available quota for that resource decreases. When you delete the resource, the quota is restored.

The following table lists the allocation quotas that apply to Agent Registry and the default value for each quota.

Quota | Value  
---|---  
Maximum agents per project | 100 (Global and per region)  
Maximum MCP servers per project | 100 (Global and per region)  
Maximum endpoints per project | 100 (Global and per region)  
Maximum bindings per project | 100 (Global and per region)  
Maximum A2A skills per project | 100 (Global and per region)  
Maximum standalone skills per project per location | 100 (Global, multi-regions, and per region)  
Maximum skill revisions per project per location, shared across all skills in the location | 500 (Global, multi-regions, and per region)  
  
## Rate quotas

Rate quotas restrict the rate at which you can consume a resource. Per-minute rate quotas reset every minute. The following table lists the rate quotas that apply to Agent Registry and the default value for each quota.

Quota | Value  
---|---  
Aggregate API requests across global and regional methods | 12,000 per minute per project (200 QPS)  
Global API requests | 1,200 per minute per project (20 QPS)  
Regional API requests | 1,200 per minute per project per region (20 QPS)  
Create, update, and delete requests for skills and skill revisions | 120 per minute per project per location (2 QPS. Global, multi-regions, and per region)  
Get, list, and search requests for skills and skill revisions | 1,200 per minute per project per location (20 QPS. Global, multi-regions, and per region)  
  
## System limits

The following table lists the system limits that apply to Agent Registry and the value for each system limit.

System limit | Value  
---|---  
Display name length | 63 characters (services and bindings); 128 characters (skills)  
Description length | 2,048 characters  
Agent specification content size | 10 KB  
MCP server specification content size | 10 KB  
Maximum compressed skill payload size (ZIP) | 1 MB  
Maximum total uncompressed skill payload size for scanned skills | 10 MB, enforced when [scanning](https://docs.cloud.google.com/agent-registry/scan-skills#payload-size-constraints) is enabled  
Maximum individual uncompressed file size in skill payload for scanned skills | 1 MB, enforced when [scanning](https://docs.cloud.google.com/agent-registry/scan-skills#payload-size-constraints) is enabled  
Maximum A2A skills or tools per service | 100  
Maximum pagination size | 100  
Maximum member projects per management project for cross-project rollup | 10,000  
  
## Agentic A2A and downstream service quotas

When your orchestrator agents discover and call [Agent2Agent (A2A)](https://docs.cloud.google.com/agent-registry/a2a-protocol) agents or Model Context Protocol (MCP) tools, Google Cloud evaluates quota consumption across three separate layers:

  * **Registry discovery and management quotas** : the allocation and rate quotas listed in this document govern only registration, management, search, and metadata lookup requests sent to Agent Registry. Runtime agent and tool calls don't consume Agent Registry rate quota after your client looks up a target agent or MCP server endpoint URL.
  * **Target agent runtime quotas** : each target runtime or Google Cloud service enforces its own rate quotas. For service-specific limits, see the quotas documentation for the target service or [view API-specific quotas](https://docs.cloud.google.com/docs/quotas/view-manage#api_specific_quota).
  * **Downstream per-service API and token quotas** : when an A2A agent calls downstream Google Cloud APIs or MCP tools, those calls consume the per-service API rate quotas of the [quota project](https://docs.cloud.google.com/docs/quotas/quota-project) or resource project billed for each request. Autonomous reasoning loops, retries, and parallel subagents can generate bursty traffic against shared project quotas. Monitor usage in [Cloud Quotas](https://docs.cloud.google.com/docs/quotas/overview) and reduce usage by requesting lower quota values as described in [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage). To help cap shared LLM token consumption across outbound agent traffic, configure [token management policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/token-management-overview) on Secure Web Proxy and Agent Gateway.



## Get quota and system limit metric names

Quotas and system limits have two types of names: display names and metric names. Display names have spaces and capitalization that make them easier for humans to read. Metric names are more likely to be lowercase and delimited by underscores instead of spaces; the exact format depends on the service.

The following instructions show how to get metric names for quotas and system limits by using either the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **IAM & Admin > Quotas & System Limits** page:

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

The table on this page displays quotas and system limits that have usage or have adjusted values, and a reference entry for other quotas. The reference entry has the word "default" in parentheses at the end of the listing in the **Name** column. For example, `SetIAMPolicy requests per minute per region (default)` is the reference entry for the quota `SetIamPolicyRequestsPerMinutePerProject`.

  2. If you don't see the **Metric** column, take the following steps.

     1. Click view_column **Column display options**.
     2. Select **Metric**.
     3. Click **OK**. The **Metric** column appears in the table.



The **Metric** column shows the metric names. To filter the results, enter a property name or value in the field next to filter_list **Filter**.

###  gcloud 

To get the metric names for a Google Cloud service by using the gcloud CLI, run the `quotas info list` command. To skip lines that don't list metric names, pass the output to a command such as `grep` with `metric:` as the search term, or use the gcloud CLI [`--format`](https://docs.cloud.google.com/sdk/gcloud/reference#--format) flag:
    
    
    gcloud beta quotas info list --project=PROJECT_ID_OR_NUMBER \
        --service=SERVICE_NAME --format="value(metric)"
    

Replace the following:

  * `PROJECT_ID_OR_NUMBER`: the project ID or project number.
  * `SERVICE_NAME`: the name of the service whose quota metrics you want to see, for example, the service name for Compute Engine is `compute.googleapis.com`. Include the `googleapis.com` portion of the service name.



## Request a quota adjustment

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics/
title: Method: projects.locations.brands.computeAnalyticsMetrics \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T06:00:16.772236+00:00
---

# Method: projects.locations.brands.computeAnalyticsMetrics  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Method: projects.locations.brands.computeAnalyticsMetrics Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * AnalyticsType
  * FeatureGate
    * JSON representation
  * AnalyticsMetrics
    * JSON representation
  * IntervalMetrics
    * JSON representation
  * PredictedFailureCategoryCount
    * JSON representation
  * MetricValue
    * JSON representation
  * OutcomeGroupCount
    * JSON representation
  * ChannelMetrics
    * JSON representation
  * UpsellMetrics
    * JSON representation
  * UpsellTypeMetrics
    * JSON representation
  * MetricMetadata
    * JSON representation



Computes analytics metrics for a given brand for specified time period with optional store filter.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{brand=projects/*/locations/*/brands/*}:computeAnalyticsMetrics`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`brand` |  `string` Required. The brand to get analytics metrics for. Format: projects/{project}/locations/{location}/brands/{brand}  
  
### Query parameters

Parameters  
---  
`timestamps[]` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The timestamps that mark the start of each interval for which analytics metrics are calculated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`storeIds[]` |  `string` Optional. The list of store IDs to get analytics metrics for. If not specified, analytics metrics for all stores will be returned. Needed to query by city or state.  
`analyticsTypes[]` |  `enum (`[AnalyticsType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#AnalyticsType)`)` Optional. The types of analytics to compute. If empty or unspecified, all available analytics types will be computed.  
`featureGate` |  `object (`[FeatureGate](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#FeatureGate)`)` Optional. Feature gates.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/ChannelType)`)` Optional. The channel type to filter analytics metrics by.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.ComputeAnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#google.cloud.foodorderingaiagent.v1.MenuService.ComputeAnalyticsMetrics)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "analyticsMetrics": {
        object ([AnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#AnalyticsMetrics))
      }
    }  
  
Fields  
---  
`analyticsMetrics` |  `object (`[AnalyticsMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#AnalyticsMetrics)`)` Output only. The analytics metrics for the brand.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## AnalyticsType

The type of analytics to compute.

Enums  
---  
`ANALYTICS_TYPE_UNSPECIFIED` | Unspecified analytics type.  
`GENERIC` | Compute generic/overall metrics (e.g., order count, escalation count, upsell count).  
`DAILY` | Compute daily metrics (e.g., daily order and escalation counts).  
`PREDICTED_FAILURE_CATEGORIES` | Compute predicted failure category metrics (e.g., predicted failure category count).  
  
## FeatureGate

Feature gates to control analytics computation behavior.

JSON representation  
---  
      
    
    {
      "enableAggregationData": boolean,
      "enableMetricsConfig": boolean
    }  
  
Fields  
---  
`enableAggregationData` |  `boolean` Optional. For limited brands only. If set, compute analytics metrics using aggregation data.  
`enableMetricsConfig` |  `boolean` Optional. If set, use the dynamic configuration-driven metrics engine.  
  
## AnalyticsMetrics

Represents analytics metrics for a given period, with a comparison to a previous period.

JSON representation  
---  
      
    
    {
      "intervalMetrics": [
        {
          object ([IntervalMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#IntervalMetrics))
        }
      ],
      "metricsMetadata": [
        {
          object ([MetricMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#MetricMetadata))
        }
      ]
    }  
  
Fields  
---  
`intervalMetrics[]` |  `object (`[IntervalMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#IntervalMetrics)`)` Metrics for the intervals.  
`metricsMetadata[]` |  `object (`[MetricMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#MetricMetadata)`)` Static display metadata for all returned metrics.  
  
## IntervalMetrics

Represents analytics metrics for a specific time interval.

JSON representation  
---  
      
    
    {
      "interval": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Interval))
      },
      "totalOrderCount": string,
      "successOrderCount": string,
      "avgOrderDurationMs": string,
      "upsellSuccessRate": number,
      "upsellRevenue": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "escalationCount": string,
      "predictedFailureCategoryCounts": [
        {
          object ([PredictedFailureCategoryCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#PredictedFailureCategoryCount))
        }
      ],
      "invalidOrderCount": string,
      "crewEscalationCount": string,
      "metrics": [
        {
          object ([MetricValue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#MetricValue))
        }
      ],
      "outcomeGroupCounts": [
        {
          object ([OutcomeGroupCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#OutcomeGroupCount))
        }
      ],
      "totalSessionCount": string,
      "avgTurnCount": number,
      "avgAgentLatencyMs": number,
      "averageOrderValue": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "channelMetrics": [
        {
          object ([ChannelMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#ChannelMetrics))
        }
      ],
      "totalOrderValue": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "upsellRate": number,
      "avgOrderValue": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "upsellMetrics": {
        object ([UpsellMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#UpsellMetrics))
      }
    }  
  
Fields  
---  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Interval)`)` The start / end time reflected by these metrics.  
`totalOrderCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total number of orders.  
`successOrderCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of successful orders.  
`avgOrderDurationMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The average order duration in ms.  
`upsellSuccessRate  
**(deprecated)**` |  `number` This item is deprecated!Output only. Deprecated: Use `upsellMetrics.upsell_success_rate` instead. The upsell success rate.  
`upsellRevenue  
**(deprecated)**` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` This item is deprecated!Output only. Deprecated: Use `upsellMetrics.upsell_revenue` instead. The upsell revenue.  
`escalationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The escalation outcome group count.  
`predictedFailureCategoryCounts[]` |  `object (`[PredictedFailureCategoryCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#PredictedFailureCategoryCount)`)` Output only. The predicted failure category counts.  
`invalidOrderCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total number of invalid orders.  
`crewEscalationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of crew escalation orders.  
`metrics[]` |  `object (`[MetricValue](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#MetricValue)`)` Output only. The dynamic metric values.  
`outcomeGroupCounts[]` |  `object (`[OutcomeGroupCount](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#OutcomeGroupCount)`)` Output only. The outcome group counts.  
`totalSessionCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total number of sessions.  
`avgTurnCount` |  `number` Output only. The average number of conversation turns per session.  
`avgAgentLatencyMs` |  `number` Output only. The average agent perceived latency in milliseconds across all turns.  
`averageOrderValue` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. The average order value across completed orders.  
`channelMetrics[]` |  `object (`[ChannelMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#ChannelMetrics)`)` Output only. Metrics broken down by channel.  
`totalOrderValue` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. The total order value across completed orders.  
`upsellRate  
**(deprecated)**` |  `number` This item is deprecated!Output only. Deprecated: Use `upsellMetrics.upsell_rate` instead. The percentage of total orders containing at least one upsell item.  
`avgOrderValue` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. The average order value across completed orders.  
`upsellMetrics` |  `object (`[UpsellMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#UpsellMetrics)`)` Output only. Consolidated upsell performance metrics for this interval.  
  
## PredictedFailureCategoryCount

Predicted failure category count.

JSON representation  
---  
      
    
    {
      "category": string,
      "count": string
    }  
  
Fields  
---  
`category` |  `string` Output only. The predicted failure category.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The count of sessions in this category.  
  
## MetricValue

Represents a single dynamic metric value.

JSON representation  
---  
      
    
    {
      "metricId": string,
      "value": number,
      "previousValue": number
    }  
  
Fields  
---  
`metricId` |  `string` Unique system identifier (e.g. "automation_rate").  
`value` |  `number` Calculated value for the metric.  
`previousValue` |  `number` Value of this metric in the previous comparison period.  
  
## OutcomeGroupCount

Outcome group count.

JSON representation  
---  
      
    
    {
      "outcomeGroup": string,
      "count": string
    }  
  
Fields  
---  
`outcomeGroup` |  `string` Output only. The outcome group label.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The count of sessions in this outcome group.  
  
## ChannelMetrics

Metrics broken down by channel.

JSON representation  
---  
      
    
    {
      "channel": string,
      "totalSessionCount": string
    }  
  
Fields  
---  
`channel` |  `string` Output only. The ordering channel (e.g. "Phone, Mobile, Drive-thru").  
`totalSessionCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total number of sessions for this channel.  
  
## UpsellMetrics

Represents upsell performance metrics for an interval.

JSON representation  
---  
      
    
    {
      "upsellRate": number,
      "upsellSuccessRate": number,
      "upsellRevenue": {
        object ([Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money))
      },
      "totalAttemptCount": string,
      "totalAcceptedCount": string,
      "typeMetrics": [
        {
          object ([UpsellTypeMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#UpsellTypeMetrics))
        }
      ]
    }  
  
Fields  
---  
`upsellRate` |  `number` Output only. Percentage of total orders containing at least one upsell item.  
`upsellSuccessRate` |  `number` Output only. Upsell conversion rate (percentage of upsell suggestions accepted).  
`upsellRevenue` |  `object (`[Money](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Money)`)` Output only. Incremental revenue lift generated from accepted upsells.  
`totalAttemptCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total upsell attempts across all types.  
`totalAcceptedCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Total accepted upsells across all types.  
`typeMetrics[]` |  `object (`[UpsellTypeMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics#UpsellTypeMetrics)`)` Output only. The upsell metrics broken down by upsell type.  
  
## UpsellTypeMetrics

Upsell metrics broken down by type.

JSON representation  
---  
      
    
    {
      "upsellType": string,
      "attemptCount": string,
      "acceptedCount": string,
      "upsellSuccessRate": number
    }  
  
Fields  
---  
`upsellType` |  `string` Output only. The upsell type (e.g. "SUGGESTIVE_UPSELL", "COMBO_UP_SIZE").  
`attemptCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of times this upsell type was attempted.  
`acceptedCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of times this upsell type was accepted.  
`upsellSuccessRate` |  `number` Output only. Conversion rate for this specific type (acceptedCount / attemptCount * 100).  
  
## MetricMetadata

Represents analytics metrics for a specific time interval. Represents the display metadata for a metric.

JSON representation  
---  
      
    
    {
      "metricId": string,
      "displayName": string,
      "description": string,
      "unit": string,
      "displayGroup": string,
      "displayOrder": integer,
      "targetThreshold": number
    }  
  
Fields  
---  
`metricId` |  `string` e.g. "automation_rate", must be unique across metrics  
`displayName` |  `string` User-friendly display name.  
`description` |  `string` Description of what the metric calculates.  
`unit` |  `string` Display unit (e.g. "%", "$", "s", "count").  
`displayGroup` |  `string` Group name for categorization in UI.  
`displayOrder` |  `integer` Display order order in dashboards.  
`targetThreshold` |  `number` The target performance threshold.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

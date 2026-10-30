---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth/
title: Method: locations.fetchServiceHealth \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T05:41:12.579167+00:00
---

# Method: locations.fetchServiceHealth  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Method: locations.fetchServiceHealth Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Granularity
  * MetricHealth
    * JSON representation
  * HistoryPoint
    * JSON representation



Fetches operational service health telemetry for a specific region.

### HTTP request

`GET https://foodorderingaiagent.googleapis.com/v1/{parent=locations/*}:fetchServiceHealth`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Format: locations/{location}  
  
### Query parameters

Parameters  
---  
`historyGranularity` |  `enum (`[Granularity](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth#Granularity)`)` Optional. Granularity of historical points. Defaults to ONE_DAY if unset.  
`lookbackDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Lookback window (e.g. 7 days, 30 days). Defaults to 7 days (168h) if unset.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`metricNames[]` |  `string` Optional. Filter by specific metric names (e.g. "foodai-service-uprate"). If empty, returns all configured health metrics for the location.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[MenuService.FetchServiceHealth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth#google.cloud.foodorderingaiagent.v1.MenuService.FetchServiceHealth)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "location": string,
      "isStale": boolean,
      "latestIntervalStart": string,
      "metrics": [
        {
          object ([MetricHealth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth#MetricHealth))
        }
      ]
    }  
  
Fields  
---  
`location` |  `string` The location requested, e.g. "locations/us".  
`isStale` |  `boolean` True if any metric's latest completed sample is older than 3 hours.  
`latestIntervalStart` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the latest completed interval included in the calculation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`metrics[]` |  `object (`[MetricHealth](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth#MetricHealth)`)` Health metrics evaluated for this location.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Granularity

Granularity of history points to return.

Enums  
---  
`GRANULARITY_UNSPECIFIED` | Unspecified granularity. Defaults to ONE_DAY.  
`ONE_HOUR` | 1-hour interval points.  
`ONE_DAY` | 1-day interval points.  
  
## MetricHealth

Health summary for a specific metric and indicator.

JSON representation  
---  
      
    
    {
      "metricName": string,
      "indicatorName": string,
      "compliancePercentage": number,
      "totalGoodCount": number,
      "totalCount": number,
      "historyPoints": [
        {
          object ([HistoryPoint](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth#HistoryPoint))
        }
      ]
    }  
  
Fields  
---  
`metricName` |  `string` The metric identifier, e.g. "foodai-service-uprate".  
`indicatorName` |  `string` The indicator name, e.g. "Availability".  
`compliancePercentage` |  `number` Aggregate compliance percentage over the lookback window: (totalGoodCount / totalCount) * 100.0. Range: [0.0, 100.0].  
`totalGoodCount` |  `number` Total good events across complete intervals in the lookback window.  
`totalCount` |  `number` Total events across complete intervals in the lookback window.  
`historyPoints[]` |  `object (`[HistoryPoint](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/locations/fetchServiceHealth#HistoryPoint)`)` Chronological history points over the requested lookback duration.  
  
## HistoryPoint

Unified history point (either daily or hourly based on requested granularity).

JSON representation  
---  
      
    
    {
      "intervalStart": string,
      "compliancePercentage": number,
      "goodCount": number,
      "totalCount": number
    }  
  
Fields  
---  
`intervalStart` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Start time of the interval.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`compliancePercentage` |  `number` Compliance percentage for this interval: (goodCount / totalCount) * 100.0. Range: [0.0, 100.0].  
`goodCount` |  `number` Number of good events in this interval.  
`totalCount` |  `number` Total number of events in this interval.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

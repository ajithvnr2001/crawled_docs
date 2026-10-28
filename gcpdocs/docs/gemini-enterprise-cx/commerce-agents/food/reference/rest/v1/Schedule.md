---
url: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule/
title: Schedule \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:10:41.916318+00:00
---

# Schedule  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Commerce agents ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)
  * [ Food AI ](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents)



Send feedback 

#  Schedule Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DateRange
    * JSON representation
  * TimeOfDayRange
    * JSON representation



A configurable schedule for one day of the week or specific date.

JSON representation  
---  
      
    
    {
      "days": [
        enum ([DayOfWeek](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/DayOfWeek))
      ],
      "dateRanges": [
        {
          object ([DateRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule#DateRange))
        }
      ],
      "timeRanges": [
        {
          object ([TimeOfDayRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule#TimeOfDayRange))
        }
      ]
    }  
  
Fields  
---  
`days[]` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/DayOfWeek)`)` Optional. The days of the week to apply the schedule to.  
`dateRanges[]` |  `object (`[DateRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule#DateRange)`)` Optional. The date ranges to apply the schedule to. If set, the schedule is only active on these specific date ranges. If both days and dateRanges are set, the schedule is active when both condition is met. For example, if days is [MONDAY] and dateRanges is [2026-01-01, 2026-01-31], the schedule is active on all Monday in January.  
`timeRanges[]` |  `object (`[TimeOfDayRange](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/v1/Schedule#TimeOfDayRange)`)` Optional. The time of day ranges to apply the schedule to. If set, the schedule is only active during these time ranges.  
  
## DateRange

Represents a date range, inclusive of both ends.

JSON representation  
---  
      
    
    {
      "startDate": {
        object ([Date](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Date))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Date))
      }
    }  
  
Fields  
---  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Date)`)` Required. The start date of the range, inclusive.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/Date)`)` Required. The end date of the range, inclusive.  
  
## TimeOfDayRange

Represents a period between two times of day on an unspecified date. For example, business hours like 09:00 to 17:00.

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeOfDay))
      },
      "endTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeOfDay))
      }
    }  
  
Fields  
---  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeOfDay)`)` Required. The start of the time range, inclusive.  
`endTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/gemini-enterprise-cx/commerce-agents/food/reference/rest/Shared.Types/TimeOfDay)`)` Required. The end of the time range, exclusive. If endTime is earlier than startTime, it means the endtime is on the next day.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

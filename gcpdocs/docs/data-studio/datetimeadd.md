---
url: https://docs.cloud.google.com/data-studio/datetimeadd/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T11:16:54.238003+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/datetimeadd/

[ Skip to main content ](https://docs.cloud.google.com/data-studio/datetimeadd/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-studio/datetimeadd/)
  * [Deutsch](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=de)
  * [Español](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=it)
  * [Português](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-studio/datetimeadd/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-studio)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/datetimeadd/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/datetimeadd/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/datetimeadd/#parameters)
  * [Return data type](https://docs.cloud.google.com/data-studio/datetimeadd/#return_data_type)
  * [Examples](https://docs.cloud.google.com/data-studio/datetimeadd/#examples)
  * [Notes](https://docs.cloud.google.com/data-studio/datetimeadd/#notes)
  * [Related resources](https://docs.cloud.google.com/data-studio/datetimeadd/#related_resources)


Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)


Send feedback 
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/datetimeadd/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/datetimeadd/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/datetimeadd/#parameters)
  * [Return data type](https://docs.cloud.google.com/data-studio/datetimeadd/#return_data_type)
  * [Examples](https://docs.cloud.google.com/data-studio/datetimeadd/#examples)
  * [Notes](https://docs.cloud.google.com/data-studio/datetimeadd/#notes)
  * [Related resources](https://docs.cloud.google.com/data-studio/datetimeadd/#related_resources)


#  DATETIME_ADD Stay organized with collections  Save and categorize content based on your preferences.
Adds a specified time interval to a date or a date and time.
## Sample usage
`DATETIME_ADD(Order Date, INTERVAL 1 WEEK)`
## Syntax
`DATETIME_ADD( datetime_expression, INTERVAL integer part )`
### Parameters
  * `datetime_expression` - a Date or a Date & Time field or expression.
  * `integer` - a whole numeric field or expression representing the number of parts to add.
  * `part` - the unit of time measurement to add. DATETIME_ADD supports the following values for `part`: 
    * `MICROSECOND`: available for Date & Time fields or expressions.
    * `MILLISECOND`: available for Date & Time fields or expressions.
    * `SECOND`: available for Date & Time fields or expressions.
    * `MINUTE`: available for Date & Time fields or expressions.
    * `HOUR`: available for Date & Time fields or expressions.
    * `DAY`
    * `WEEK`: This date part begins on Sunday.
    * `ISOWEEK`: Uses [ISO 8601 week](https://en.wikipedia.org/wiki/ISO_week_date) boundaries. ISO weeks begin on Monday.
    * `MONTH`
    * `QUARTER`
    * `YEAR`
    * `ISOYEAR`: Uses the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) week-numbering year boundary. The ISO year boundary is the Monday of the first week whose Thursday belongs to the corresponding Gregorian calendar year.


## Return data type
Date & Time
## Examples  
| Example formula  | Output  |  
| --- | --- |  
|  `DATETIME_ADD(DATETIME "2023-01-25 15:30:00", INTERVAL 10 MINUTE)`  |  Jan 25, 2023, 3:40:00 PM   |  
|  `DATETIME_ADD(DATE "2023-01-25", INTERVAL 5 DAY)`  |  Jan 30, 2023, 12:00:00 AM   |  
## Notes
This function is not available for compatibility mode date types.
When using `MONTH`, `QUARTER`, or `YEAR` parts, if the resulting date is at (or near) the last day of the month, `DATETIME_ADD` returns the last day of the month. This can happen when the month in the resulting date has fewer days than the month in the starting date.
For example, if **Date** = August 31, 2020, `DATETIME_ADD(Date, INTERVAL 1 MONTH)` returns September 30, 2020.
## Related resources
  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

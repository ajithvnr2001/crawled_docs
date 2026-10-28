---
url: https://docs.cloud.google.com/data-studio/minute/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:11:09.711172+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/minute/

[ Skip to main content ](https://docs.cloud.google.com/data-studio/minute/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-studio/minute/)
  * [Deutsch](https://docs.cloud.google.com/data-studio/minute/?hl=de)
  * [Español](https://docs.cloud.google.com/data-studio/minute/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-studio/minute/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-studio/minute/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-studio/minute/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-studio/minute/?hl=it)
  * [Português](https://docs.cloud.google.com/data-studio/minute/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-studio/minute/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-studio/minute/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-studio/minute/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-studio/minute/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-studio/minute/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-studio/minute/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fdata-studio%2Fminute%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-studio)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/minute/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/minute/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/minute/#parameters)
  * [Examples](https://docs.cloud.google.com/data-studio/minute/#examples)
  * [Notes](https://docs.cloud.google.com/data-studio/minute/#notes)
  * [Related resources](https://docs.cloud.google.com/data-studio/minute/#related_resources)


Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)


Was this helpful?
Send feedback 
  * On this page
  * [Sample usage](https://docs.cloud.google.com/data-studio/minute/#sample_usage)
  * [Syntax](https://docs.cloud.google.com/data-studio/minute/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/minute/#parameters)
  * [Examples](https://docs.cloud.google.com/data-studio/minute/#examples)
  * [Notes](https://docs.cloud.google.com/data-studio/minute/#notes)
  * [Related resources](https://docs.cloud.google.com/data-studio/minute/#related_resources)


#  MINUTE Stay organized with collections  Save and categorize content based on your preferences.
Returns the minutes component of a given date.
## Sample usage
`MINUTE(Date_Time)`
## Syntax
1) Returns the minute from a Date & Time value.
`MINUTE( date_expression )`
2) Returns the minute from a compatibility mode Date value.
`MINUTE( X [, format_string ])`
### Parameters
  * `date_expression` - a Date & Time field or expression.
  * `X` - a field or expression that evaluates to Text, Number, or compatibility mode Date.
  * `format_string` - format for `X`. Optional if `X` is correctly configured as a semantic date field.


Input format for compatibility mode dates 
Supported date functions accept the following input formats if `X` is a Text field or expression, or compatibility mode Date:
  * Any valid [strptime](http://pubs.opengroup.org/onlinepubs/009695399/functions/strptime.html) format is accepted.
  * `'BASIC':`%Y/%m/%d-%H:%M:%S
  * `'DEFAULT_DASH':`%Y-%m-%d [%H:%M:%S]
  * `'DEFAULT_SLASH':`%Y/%m/%d [%H:%M:%S]
  * `'DEFAULT_DECIMAL':`%Y%m%d [%H:%M:%S]
  * `'RFC_1123':`for example,  Sat, 24 May 2008 20:09:47 GMT 
  * `'RFC_3339':`for example, 2008-05-24T20:09:47Z
  * `'DECIMAL_DATE':`same as `'DEFAULT_DECIMAL'`


Supported time functions accept the following input format if `X` is a Number field or expression:
  * `'SECONDS':`seconds since Epoch
  * `'MILLIS':`milliseconds since Epoch
  * `'MICROS': `microseconds since Epoch
  * `'NANOS':`nanoseconds since Epoch
  * `'JULIAN_DATE':`days since Epoch


## Examples  
| Example formula  | Input  | Output  |  
| --- | --- | --- |  
|  ` MINUTE(Date) `  |  Jan 1, 2019   |  0   |  
|  ` MINUTE(Date as Text, 'BASIC') `  |  2019/01/01-09:40:45   |  40   |  
|  ` MINUTE(Date as Number, 'SECONDS') `  |  1561784874   |  7   |  
|  ` MINUTE(Date as lots of Numbers, 'MILLIS') `  |  1562004058620   |  0   |  
## Notes
This function works with both compatibility mode dates and [upgraded Date and Date & Time](https://docs.cloud.google.com/data-studio/dates-and-times) data types.
## Related resources
  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/data-studio/countdistinct/
title: COUNT_DISTINCT \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T11:16:53.417015+00:00
---

# COUNT_DISTINCT  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/countdistinct/

[ Skip to main content ](https://docs.cloud.google.com/data-studio/countdistinct/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/data-studio/countdistinct/)
  * [Deutsch](https://docs.cloud.google.com/data-studio/countdistinct/?hl=de)
  * [Español](https://docs.cloud.google.com/data-studio/countdistinct/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/data-studio/countdistinct/?hl=es-419)
  * [Français](https://docs.cloud.google.com/data-studio/countdistinct/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/data-studio/countdistinct/?hl=id)
  * [Italiano](https://docs.cloud.google.com/data-studio/countdistinct/?hl=it)
  * [Português](https://docs.cloud.google.com/data-studio/countdistinct/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/data-studio/countdistinct/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/data-studio/countdistinct/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/data-studio/countdistinct/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/data-studio/countdistinct/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/data-studio/countdistinct/?hl=ja)
  * [한국어](https://docs.cloud.google.com/data-studio/countdistinct/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/data-analytics-color.svg) ](https://docs.cloud.google.com/data-studio)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Syntax](https://docs.cloud.google.com/data-studio/countdistinct/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/countdistinct/#parameters)
  * [How the COUNT_DISTINCT function works](https://docs.cloud.google.com/data-studio/countdistinct/#how_the_count_distinct_function_works)
  * [Examples](https://docs.cloud.google.com/data-studio/countdistinct/#examples)
  * [Limits of COUNT_DISTINCT](https://docs.cloud.google.com/data-studio/countdistinct/#limits_of_count_distinct)
    * [COUNT_DISTINCT works with unaggregated data](https://docs.cloud.google.com/data-studio/countdistinct/#count_distinct_works_with_unaggregated_data)
    * [Consider using APPROX_COUNT_DISTINCT for BigQuery data](https://docs.cloud.google.com/data-studio/countdistinct/#bq-approx)
    * [Variable results from function pushdown](https://docs.cloud.google.com/data-studio/countdistinct/#variable_results_from_function_pushdown)
  * [Related resources](https://docs.cloud.google.com/data-studio/countdistinct/#related_resources)


Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)


Send feedback 
#  COUNT_DISTINCT Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Syntax](https://docs.cloud.google.com/data-studio/countdistinct/#syntax)
    * [Parameters](https://docs.cloud.google.com/data-studio/countdistinct/#parameters)
  * [How the COUNT_DISTINCT function works](https://docs.cloud.google.com/data-studio/countdistinct/#how_the_count_distinct_function_works)
  * [Examples](https://docs.cloud.google.com/data-studio/countdistinct/#examples)
  * [Limits of COUNT_DISTINCT](https://docs.cloud.google.com/data-studio/countdistinct/#limits_of_count_distinct)
    * [COUNT_DISTINCT works with unaggregated data](https://docs.cloud.google.com/data-studio/countdistinct/#count_distinct_works_with_unaggregated_data)
    * [Consider using APPROX_COUNT_DISTINCT for BigQuery data](https://docs.cloud.google.com/data-studio/countdistinct/#bq-approx)
    * [Variable results from function pushdown](https://docs.cloud.google.com/data-studio/countdistinct/#variable_results_from_function_pushdown)
  * [Related resources](https://docs.cloud.google.com/data-studio/countdistinct/#related_resources)


The `COUNT_DISTINCT` function counts the number of unique items in a field.
## Syntax
`COUNT_DISTINCT(X)`
### Parameters
  * `X` - a field or an expression that contains the items to be counted.


## How the `COUNT_DISTINCT` function works
The `COUNT_DISTINCT` function takes one parameter, which can be the name of a dimension or an expression that doesn't result in an aggregation. `COUNT_DISTINCT` returns the total number of unique items in that field or expression.
To count all items, including duplicates, use `COUNT`. 
## Examples  
|  Example formula   |  Output   |  
| --- | --- |  
|  ` COUNT_DISTINCT(user_id) `  |  22,854,921   |  
|  ` COUNT_DISTINCT(order_id) `  |  497,091,812   |  
## Limits of `COUNT_DISTINCT`
When using the `COUNT_DISTINCT` function, note the following:
###  `COUNT_DISTINCT` works with unaggregated data
You can't apply this function to metrics, including fields with an **Aggregation** type of **Auto** , or to an expression that's the result of another aggregation function. For example, a formula such as `COUNT_DISTINCT(Sessions)` in a Google Analytics data source produces an error because `Sessions` is an **Auto** aggregated field.
### Consider using `APPROX_COUNT_DISTINCT` for BigQuery data
To avoid possibly incurring higher query costs when using BigQuery data sources, consider using `APPROX_COUNT_DISTINCT`.
### Variable results from function pushdown
To optimize performance, Data Studio attempts to delegate (or "push down") the calculation of `COUNT_DISTINCT` to the underlying data source whenever possible. Because the actual count is performed by the connected system rather than by Data Studio, the results can vary depending on how that system implements distinct counting.
For example, factors that can lead to differences in distinct counts include the following:
  * **SQL databases** : Different SQL dialects may handle case-sensitivity, trailing space comparison, or null value counting in unique ways.
  * **File-based sources** : For file connectors (such as CSV files), results depend on target-site parsing behavior and internal engine operations.
  * **SaaS APIs** : Cloud services and SaaS connectors are constrained by their API capabilities, which may return approximate counts or apply specific filtering logic.


## Related resources
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

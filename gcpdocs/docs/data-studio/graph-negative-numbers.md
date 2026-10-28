---
url: https://docs.cloud.google.com/data-studio/graph-negative-numbers/
title: Graph negative numbers \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: httpx+scrapegraph (scrapling: scrapling status 429 | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 1299 in create_browser_context (../../../../usr/local/lib/python3.10/dist-packages/crawl4ai/browser_manager.py):
Error: Browser is not available. It may have been closed, crashed, or not yet started. Ensure the browser is running before creating new contexts.

Code context:
1294                   raise RuntimeError(
1295                       "Cannot create new browser contexts when using "
1296                       "use_persistent_context=True. Persistent context uses a "
1297                       "single shared context."
1298                   )
1299 →             raise RuntimeError(
1300                   "Browser is not available. It may have been closed, crashed, "
1301                   "or not yet started. Ensure the browser is running before "
1302                   "creating new contexts."
1303               )
1304           # Base settings)
fetched_at: 2026-10-27T16:21:50.344355+00:00
---

# Graph negative numbers  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/graph-negative-numbers/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Graph negative numbers Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** As of 2019-01-16, the default value for Axis min is (auto), so you'll only need to change this for older charts. The previous default Axis min setting was "0."

To display metrics with negative values in a chart, set the **Axis min** option to **(auto)** :

  1. Edit your report.
  2. Select the chart.
  3. Select the STYLE panel.
  4. Locate the main axis settings: for default charts, this will be the left axis, but could also be right or bottom, depending on how you've customized your chart.
  5. Change the **Axis min** value to **(auto)** by deleting the current setting.



Here's an example of how charts look with Axis min 0 versus Axis min (auto):

![Six column charts organized into two columns of three charts. The first column displays charts with the Axis Min set to 0, and the second column displays charts with the Axis Min set to auto.](https://docs.cloud.google.com/static/data-studio/images/axis-min-auto-2019-01-17.png)

  1. Data in the top charts contains mixed negative and positive values. 
     1. Charts on the left are set to use **Axis min: 0**.
     2. Charts on the right use **Axis min: (auto)**.
     3. Note how the last two dimension values ("  Green  " and "  Blue  ") appear in the charts.
  2. Data in the middle charts only contains positive values. In this case, there is no difference between 0 and (auto) settings.
  3. Data in the bottom charts only contains negative values. Here, using the (auto) setting on the right provides the correct visualization.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

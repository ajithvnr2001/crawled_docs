---
url: https://docs.cloud.google.com/error-reporting/docs/setup/cloud-run/
title: Setting up on Cloud Run \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:27:37.122711+00:00
---

# Setting up on Cloud Run  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/setup/cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Setting up on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Error Reporting lets you monitor and diagnose application crashes in Cloud Run by automatically detecting stack traces written to `stdout` or `stderr`. If exceptions aren't detected, then you can [instrument your service](https://docs.cloud.google.com/error-reporting/docs/setup#libraries) with Error Reporting client libraries or [manually format error messages](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages) in Cloud Logging.

## Viewing errors

To view exception logs in Cloud Run, go to the **Metrics** tab of the [service detail page](https://docs.cloud.google.com/run/docs/managing/services#details). It includes a table showing the top errors for Cloud Run that Error Reporting has detected and aggregated.

For instructions on viewing error and exception data for your application in the Google Cloud console, go to [Viewing errors](https://docs.cloud.google.com/error-reporting/docs/viewing-errors).

**Note** : If you see the message "Set up Error Reporting" on the **Error Reporting** page, then your Google Cloud project has no error groups to display.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

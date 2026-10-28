---
url: https://docs.cloud.google.com/integration-connectors/docs/quotas/
title: Limits \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:27:57.100618+00:00
---

# Limits  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Resources ](https://docs.cloud.google.com/integration-connectors/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Limits

This page lists the known limitations for Integration Connectors.

Integration Connectors enforces the following usage limits. You are responsible for tracking and ensuring that the values stay within the prescribed limits.

Resource | Limit | Value  
---|---|---  
All connections | Maximum number of connections per region | 50  
Maximum number of [nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) per connection | 100  
Maximum payload size supported by the [Connectors task in Application Integration](https://docs.cloud.google.com/application-integration/docs/quotas#data-processing-limits) | 10 MB  
Regions | You can use a maximum of 20 unique regions to configure all your connections. For example, if you have created 20 connections where each connection uses a different region, you can't create a new 21st connection in a different region. The new connection must use any one of your 20 regions that you are already using. | N/A  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

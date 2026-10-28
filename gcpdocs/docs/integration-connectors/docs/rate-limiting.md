---
url: https://docs.cloud.google.com/integration-connectors/docs/rate-limiting/
title: Rate limiting connection traffic \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:27:00.191442+00:00
---

# Rate limiting connection traffic  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/rate-limiting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Rate limiting connection traffic

This page describes how Integration Connectors rate limits (controls) the incoming requests to your connection, and the various options available to you to address the rate limit conditions that may occur in your connection.

Integration Connectors intelligently manages a connection's traffic by throttling (smoothening traffic spikes) requests from a connection. So, suppose there is an increase in a connection's traffic; Integration Connectors automatically increases the number of nodes assigned to the connection, and conversely, if there is a drop in a connection's traffic, Integration Connectors automatically decreases the number of nodes assigned to the connection. This node autoscaling ensures that a connection's node allocation is always optimal.

However, in some scenarios, it is possible that a connection uses all its available nodes and still requires additional nodes. In such a scenario, where a connection exceeds its throttling limits, Integration Connectors returns the `HTTP 429` response.

Your options for rate limiting a connection vary based on your user type (pay-as-you-go or subscription) as described in the following sections.

## Rate limiting for pay-as-you-go users

Scenario |  | Remediation | Are you anticipating or seeing a spike in your connection's traffic? | Yes | Integration Connectors autoscales the connection nodes till it reaches the configured maximum node limit. However, based on your traffic pattern, you can proactively configure the required minimum and maximum nodes for the connection in the [Edit connection page](https://docs.cloud.google.com/integration-connectors/docs/editconnection).   
---|---|---  
No | No action required from you.  
Are you getting the `HTTP 429` response for your connection? | Yes | Even though the connection nodes are autoscaled, you may have encountered the following scenarios: 

  * There is a sudden spike in the connection's traffic which the existing nodes can't handle, and hence you are temporarily getting this error. In this case, increase the number of minimum nodes for the connection in the [Edit connection page](https://docs.cloud.google.com/integration-connectors/docs/editconnection).
  * The maximum permissible node limit isn't fully utilized by the connection. In this case, increase the maximum nodes in the [Edit connection page](https://docs.cloud.google.com/integration-connectors/docs/editconnection).
  * The maximum node limit is fully utilized by the connection. In this case, contact [Integration Connectors support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).

**Tip** : You can re-run your integration by using any of the retry strategies. For more information, see [Error handling strategies in Application Integration](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).  
No | No action required from you.  
  
## Rate limiting for subscription users

Scenario |  | Remediation | Are you anticipating or seeing a spike in your connection's traffic? | Yes | No action required from you. Integration Connectors autoscales the connection nodes which in turn takes care of throttling.  
---|---|---  
No | No action required from you.  
Are you getting the `HTTP 429` response for your connection? | Yes | Contact [Integration Connectors support](https://docs.cloud.google.com/integration-connectors/docs/getting-support). **Tip** : You can re-run your integration by using any of the retry strategies. For more information, see [Error handling strategies in Application Integration](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).  
No | No action required from you.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

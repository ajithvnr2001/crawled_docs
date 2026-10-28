---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-multiple-plugin-versions/
title: Manage multiple versions of the same plugin \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:34:34.621971+00:00
---

# Manage multiple versions of the same plugin  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/manage-multiple-plugin-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage multiple versions of the same plugin Stay organized with collections  Save and categorize content based on your preferences. 

If you have multiple versions of the same plugin in the Cloud Data Fusion Studio, you can select which one you want to use in a data pipeline. If you upgrade a Cloud Data Fusion instance without upgrading the pipelines, there are typically multiple versions of the plugins present.

**Note:** Only one plugin version can be used per pipeline. For example, you cannot have both BigQuery batch source 0.16.2 and BigQuery batch source 0.17.1 in the same pipeline.

To set the default version of a plugin, follow these steps:

  1. Go to your instance: 

     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. To open the instance in the Cloud Data Fusion Studio, click **Instances** , and then click **View instance**.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the Cloud Data Fusion Studio interface, click **Studio**.

  3. In the plugins list, hold the pointer over a plugin, such as the BigQuery batch source plugin, and click more_vert **More**.

  4. To change the default version of the plugin, click **Change** next to the current version of the plugin.

**Note:** If you don't see the **Change** option, you have only one version of the plugin in your namespace.
  5. Click the version of the plugin you want to use in the pipeline.This version becomes the default version of the plugin for all pipelines.




## What's next

  * Learn more about [plugin drivers](https://docs.cloud.google.com/data-fusion/docs/how-to/using-jdbc-drivers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

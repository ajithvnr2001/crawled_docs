---
url: https://docs.cloud.google.com/endpoints/docs/grpc/quotas-override/
title: Overriding the default quota limit \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:25:16.292591+00:00
---

# Overriding the default quota limit  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/quotas-override/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Overriding the default quota limit Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-override "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you configure a quota, the limit applies to all applications that call your API. The **Endpoints Services** page displays the quotas configured for each method in your API under **Quotas** > **Default quotas**. If needed, you can set a different limit for a specific consumer project.

To override the default quota limit:

  1. Get the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project whose limit you want to override. If you don't have permission to access the API consumer's project, ask someone who has permission to get the project number for you.
  2. In the Google Cloud console, go to the **Endpoints Services** page for your project.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  3. If you have more than one API, select the API that you want to configure from the list.

  4. Click the **Quotas** tab.

  5. Under **Project quotas** , enter the project number and click **View project quotas**.

  6. For the quota you want to change, click **Edit limit**.

  7. In the **Edit limit** dialog box that displays, click **Custom** and enter the new limit.

  8. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

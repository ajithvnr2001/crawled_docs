---
url: https://docs.cloud.google.com/healthcare-api/docs/deprecations/
title: Feature deprecations \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:31:25.124195+00:00
---

# Feature deprecations  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/deprecations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Resources ](https://docs.cloud.google.com/healthcare-api/docs/resources)



Send feedback 

#  Feature deprecations Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to the Cloud Healthcare API. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

Feature | Deprecated date | Decommissioned date | Details  
---|---|---|---  
**Google Cloud Healthcare Annotations API** | May 16, 2023 | May 30, 2025 | The Google Cloud Healthcare Annotations API is deprecated. As an alternative, you can save annotation data for de-identified images using FHIR resources. For more information, see [Write de-identify operation metadata to a FHIR store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-annotation).  
**Healthcare Natural Language API** | May 27, 2025 |  | The Healthcare Natural Language API is deprecated. As an alternative, you can use a Generally Available (GA) Gemini model on Vertex AI. For more information, see [Generally available Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#generally_available_models).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

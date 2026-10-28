---
url: https://docs.cloud.google.com/armor/docs/apis/
title: APIs and references \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:18:31.119756+00:00
---

# APIs and references  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Reference ](https://docs.cloud.google.com/armor/docs/apis)



Send feedback 

#  APIs and references Stay organized with collections  Save and categorize content based on your preferences. 

You configure Google Cloud Armor security policies and rules using API resources that are part of the Compute Engine API and the Google Cloud CLI. This page lists the API resources and Google Cloud CLI command groups that you use to configure Cloud Armor.

  * **Security policies** : Use to create security policies and rules.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies) | [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies)

  * **Hierarchical Security policies** : Use to create hierarchical security policies and rules.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/org-security-policies) | [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/organizationSecurityPolicies)

  * **Backend services** : Use to attach a security policy to a backend service.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services) | [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices)




To learn how to write expressions in advanced match conditions for security policy rules, see the [Cloud Armor custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

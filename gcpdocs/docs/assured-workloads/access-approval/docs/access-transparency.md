---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/access-transparency/
title: Introduction to Access Transparency \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:22:29.159810+00:00
---

# Introduction to Access Transparency  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/access-transparency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to Access Transparency

As a part of Google's long-term commitment to security and transparency, Access Transparency lets you review logs of actions that Google personnel take when accessing certain customer content to fulfill their contractual obligations.

Access Transparency logs include information about Google personnel activity, including the following:

  * Actions taken by the Cloud Customer Care team to resolve a support ticket that you filed.
  * Investigation of an outage.



For more information, see [Overview of Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview).

To learn about the core principles upon which controls that prevent unauthorized administrative access are based, see [Overview of administrative access controls](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access).

For the list of services that Access Transparency supports, see [Supported services](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services).

For information about Google Cloud's approach to privileged access management, see [Privileged access at Google Cloud](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/privileged-access).

## Get started with using Access Transparency

Learn how to [enable Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable). Then, [understand and use Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

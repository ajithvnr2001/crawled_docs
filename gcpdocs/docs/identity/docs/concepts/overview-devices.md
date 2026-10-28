---
url: https://docs.cloud.google.com/identity/docs/concepts/overview-devices/
title: Devices API overview \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:30:57.338398+00:00
---

# Devices API overview  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/overview-devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Devices API overview

The Cloud Identity Devices API lets you create and manage different types of devices within your organization. Supported devices include Android, iOS (With Fundamental, Basic or Advanced management) and desktop devices, including those with Enhanced Desktop Security for Windows, Endpoint Verification, or Drive File Stream.

With the Devices API, you can:

  * Manage personal and company-owned devices.
  * Manage organizational user accounts on devices.
  * Perform actions, such as wipe a device or remote sign-out, on devices.
  * Search for devices and organizational user accounts on devices.
  * Manage custom state with each user account. This state can be used to evaluate Context Aware Access levels.



## Next steps

Here are a few next steps you might take:

  * To set up Cloud Identity, refer to [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).
  * To set up the Devices API, refer to [Setting up the Devices API](https://docs.cloud.google.com/identity/docs/how-to/setup-devices).
  * To create a device, refer to [Create a device](https://docs.cloud.google.com/identity/docs/how-to/create-devices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

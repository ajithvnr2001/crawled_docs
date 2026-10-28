---
url: https://docs.cloud.google.com/filestore/docs/mount-latency/
title: Troubleshoot latency issues when mounting or unmounting \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
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
fetched_at: 2026-10-27T16:24:56.696245+00:00
---

# Troubleshoot latency issues when mounting or unmounting  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/mount-latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot latency issues when mounting or unmounting Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting information to help address latency issues you might encounter while using Filestore.

## Latency when mounting and unmounting a file share

When mounting a file share using the default mount options, the mount command attempts to discover the supported transport method of the Filestore instance, which introduces a three-second latency.

The `mountd` daemon first tries to use UDP, which Filestore doesn't support. Once the initial try times out, it falls back to TCP. To bypass this discovery process and eliminate the added latency, you can specify the `tcp` mount option, for example:
    
    
    sudo mount -o tcp 10.0.0.2:/vol1 /mnt/nfs
    

This mount option is especially important if you're [automounting with `autofs`](https://docs.cloud.google.com/filestore/docs/mounting-fileshares#linux:-autofs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

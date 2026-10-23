---
url: https://developer.android.com/develop/connectivity/cronet/
title: Perform network operations using Cronet \u00a0|\u00a0 Connectivity \u00a0|\u00a0 Android Developers
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:44:05.145307+00:00
---

# Perform network operations using Cronet  |  Connectivity  |  Android Developers

> Source: https://developer.android.com/develop/connectivity/cronet/

  * [ Android Developers ](https://developer.android.com/)
  * [ Develop ](https://developer.android.com/develop)
  * [ Core areas ](https://developer.android.com/develop/core-areas)
  * [ Connectivity ](https://developer.android.com/develop/connectivity)
  * [ Guides ](https://developer.android.com/develop/connectivity/overview)



#  Perform network operations using Cronet Stay organized with collections  Save and categorize content based on your preferences. 

Cronet is the Chromium network stack made available to Android apps as a library. Cronet takes advantage of multiple technologies that reduce the latency and increase the throughput of the network requests that your app needs to work.

The Cronet Library handles the requests of apps used by millions of people on a daily basis, such as [YouTube](https://play.google.com/store/apps/details?id=com.google.android.youtube), [Google App](https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox), [Google Photos](https://play.google.com/store/apps/details?id=com.google.android.apps.photos), and [Maps - Navigation & Transit](https://play.google.com/store/apps/details?id=com.google.android.apps.maps).

## Features

**Protocol support**
    Cronet natively supports the [HTTP](https://tools.ietf.org/html/rfc2616), [HTTP/2](https://tools.ietf.org/html/rfc7540), and [HTTP/3 over QUIC](https://www.chromium.org/quic) protocols.
**Request prioritization**
    The library allows you to set a priority tag for the requests. The server can use the priority tag to determine the order in which to handle the requests.
**Resource caching**
    Cronet can use an in-memory or disk cache to store resources retrieved in network requests. Subsequent requests are served from the cache automatically.
**Asynchronous requests**
    Network requests issued using the Cronet Library are asynchronous by default. Your worker threads aren't blocked while waiting for the request to come back.
**Data compression**
    Cronet supports data compression using the [Brotli Compressed Data Format](https://tools.ietf.org/html/rfc7932).

To learn how to use the Cronet Library in your app for Android, see [Send a simple request](https://developer.android.com/develop/connectivity/cronet/start). You can also browse the [Cronet Sample](https://github.com/GoogleChromeLabs/cronet-sample) on GitHub.

You can send feedback about the Cronet Library using the [Chromium Issue Tracker](https://crbug.com). Check the list of bugs in the issue tracker to make sure that your issue hasn't already been reported. If your issue hasn't been reported, file a bug with the word _Cronet_ in the summary line.

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 

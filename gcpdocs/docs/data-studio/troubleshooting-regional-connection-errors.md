---
url: https://docs.cloud.google.com/data-studio/troubleshooting-regional-connection-errors/
title: Troubleshooting regional connection errors \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-04T05:36:24.795277+00:00
---

# Troubleshooting regional connection errors  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/troubleshooting-regional-connection-errors/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Troubleshooting regional connection errors Stay organized with collections  Save and categorize content based on your preferences. 

If you're using Data Studio outside of the United States, you might encounter the following errors when attempting to view charts:

  * `[server IP address]'s server IP address could not be found`
  * `[URL] Web page may be temporarily down or moved permanently`



These errors can occur if your local Internet Service Provider (ISP) is missing Domain Name System (DNS) entries for `*.scf.usercontent.goog`, which is required for chart rendering. To resolve this issue, you can update your network configuration using one of the following methods:

## Method 1: Use Google Public DNS (Recommended)

By changing your network settings to use Google Public DNS (`8.8.8.8` or `8.8.4.4`), your system resolves domain names against Google's global servers rather than your local ISP. Because Google's DNS servers correctly list all required subdomains, your browser can successfully locate the rendering servers and load charts.

## Method 2: Configure manual IP mapping using a proxy or PAC file

If you can't change your system DNS settings, you can update your proxy settings or Proxy Auto-Configuration (PAC) file to route requests for `scf.usercontent.goog` directly to the IP address `142.251.46.225`. This allows your browser to bypass the DNS lookup step and connect directly to the rendering server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-03 UTC."],[],[]] 

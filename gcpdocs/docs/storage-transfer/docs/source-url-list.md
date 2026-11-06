---
url: https://docs.cloud.google.com/storage-transfer/docs/source-url-list/
title: Configure access to a source: URL list \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T10:53:04.182382+00:00
---

# Configure access to a source: URL list  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-url-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: URL list Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the requirements for transferring data from a publicly accessible list of HTTP/HTTPS URLs to Cloud Storage.

Transfers from a URL list are agentless transfers managed directly by Storage Transfer Service.

## Prerequisites

Before creating a transfer from a URL list, ensure that you have configured the following:

  * **User permissions:** Ensure your user account or user-managed service account has permission to create transfer jobs. See [Required user permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-user).
  * **Destination bucket permissions:** Grant the required permissions on your destination Cloud Storage bucket to the Storage Transfer Service service agent. See [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).
  * **URL list stored in Cloud Storage (optional):** If you store your URL list file in a Cloud Storage bucket rather than a public HTTP/HTTPS URL, grant the Storage Transfer Service service agent `roles/storage.objectViewer` and `roles/storage.legacyBucketReader` on that bucket. See [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage).



## Source URL requirements

To allow Storage Transfer Service to read your source data, ensure that the following requirements are met:

  * **Public accessibility:**

    * The URL list file (TSV format) must be accessible from a URL beginning with either `http://` or `https://`, or stored in a Cloud Storage bucket.
    * Each object URL listed in the file must be publicly accessible via `http://` or `https://`.
  * **Web server configuration:**

    * The web server hosting each object must support HTTP `Range` requests to allow parallel chunked transfers.
    * The web server must return a valid `Content-Length` header in each response.
    * The web server's `robots.txt` file must allow access to the URLs for the `Google-Storage-Transfer-Service` user agent or all user agents (`*`).
  * **Object size and checksum validation:**

    * If you specify object sizes or MD5 checksums in your URL list, ensure that the values match the actual object payloads returned by the server. If the size or checksum does not match, the transfer of that object fails.



## What's next

  * [Create a transfer from a URL list](https://docs.cloud.google.com/storage-transfer/docs/create-url-list).
  * Learn more about the [URL list file format](https://docs.cloud.google.com/storage-transfer/docs/create-url-list#url-list-format).
  * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage).
  * Review the [Role and permission reference](https://docs.cloud.google.com/storage-transfer/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-05 UTC."],[],[]] 

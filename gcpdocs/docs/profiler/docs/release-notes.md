---
url: https://docs.cloud.google.com/profiler/docs/release-notes/
title: Profiler release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-03T09:44:21.709639+00:00
---

# Profiler release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Resources ](https://docs.cloud.google.com/profiler/quotas)



Send feedback 

#  Profiler release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Profiler. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

For a combined list of all release notes for the products in Google Cloud Observability, see [Consolidated release notes](https://docs.cloud.google.com/stackdriver/docs/release-notes).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml) directly. 

## October 29, 2026

Security

The Cloud Profiler Java agent is updated with a new Certification Authority (CA) certificate bundle, in response to security bulletin [GCP-2026-071](https://docs.cloud.google.com/support/bulletins#gcp-2026-071). Google Cloud infrastructure and the Cloud Profiler backend service are not affected.

If you use the Cloud Profiler Java agent, take one of the following actions:

  * Upgrade the Java agent to `cloud-profiler-java-agent_20261026_RC00` ([GitHub release v0.5.0](https://github.com/GoogleCloudPlatform/cloud-profiler-java/releases/tag/v0.5.0)) or later, and then rebuild and redeploy your applications. Download the updated archive, <https://storage.googleapis.com/cloud-profiler/java/cloud-profiler-java-agent_20261026_RC00.tar.gz>, or, for `musl`-based Alpine Linux containers, <https://storage.googleapis.com/cloud-profiler/java/cloud-profiler-java-agent_20261026_RC00_alpine.tar.gz>.
  * If you can't immediately upgrade or rebuild, update your host or container operating system's CA certificate store as described in [GCP-2026-071](https://docs.cloud.google.com/support/bulletins#gcp-2026-071), and then set the `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` environment variable to point to the updated PEM bundle.



For more information about installing the agent, see [Profiling Java applications](https://docs.cloud.google.com/profiler/docs/profiling-java#installing-profiler).

## September 29, 2020

Feature

Cloud Profiler history view is available in beta. For more information, see [Viewing historical trends](https://cloud.google.com/profiler/docs/history-view).

## May 12, 2020

Change

The Cloud Profiler Python agent is now generally available. See [Profiling Python applications](https://cloud.google.com/profiler/docs/profiling-python) for information on configuring your Python application.

## April 20, 2020

Change

The Cloud Profiler Node.js agent no longer supports release 8 of Node.js.

Change

The Cloud Profiler Node.js agent is now generally available. See [Profiling Node.js applications](https://cloud.google.com/profiler/docs/profiling-nodejs) for information on configuring your Node.js application.

Feature

The Cloud Profiler Node.js agent now supports release 12 of Node.js. See [Profiling Node.js applications](https://cloud.google.com/profiler/docs/profiling-nodejs) for information on configuring your Node.js application.

## March 24, 2020

Change

Integration of Stackdriver Profiler with Virtual Private Cloud Service Controls is now Generally Available. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## December 13, 2019

Feature

Strackdriver Profiler supports Istio on Google Kubernetes Engine for [Go](https://cloud.google.com/profiler/docs/profiling-go), [Java](https://cloud.google.com/profiler/docs/profiling-java), [Python](https://cloud.google.com/profiler/docs/profiling-python), and [Node.js](https://cloud.google.com/profiler/docs/profiling-nodejs) services. This feature is now in **Beta**.

## December 10, 2019

Feature

Integration of Stackdriver Profiler with Virtual Private Cloud Service Controls is now beta. For more information, see [VPC Service Controls documentation](https://cloud.google.com/vpc-service-controls/docs/).

## May 08, 2019

Feature

Java 11 is now supported. For more information, see [Profiling Java](https://cloud.google.com/profiler/docs/profiling-java).

## March 26, 2019

Feature

Stackdriver Profiler is now generally available. Stackdriver Profiler lets you analyze and understand the performance of your Go, Java, Node.js or Python applications. For more information, see [About Stackdriver Profiler](https://cloud.google.com/profiler/docs/about-profiler).

## March 12, 2019

Feature

Python is now supported. For more information, see [Profiling Python](https://cloud.google.com/profiler/docs/profiling-python).

## February 28, 2019

Feature

The new **Color mode** filter option lets you color the flame graph frames by package name, by the metric consumption of the function, or by the metric consumption of the function and its children. For more information, see [Color mode](https://cloud.google.com/profiler/docs/filtering-profiles#color-filter).

## December 07, 2018

Feature

Go 1.11 for App Engine standard environment is now supported. For more information, see [Profiling Go](https://cloud.google.com/profiler/docs/profiling-go).

## August 02, 2018

Feature

The new **Weight** filter lets you select and graph profiles that consume the most of the profile's measured metric. For more information, see [Weight filter](https://cloud.google.com/profiler/docs/selecting-profiles#weight-filter).

## July 24, 2018

Feature

The new **Compare To** option lets you compare profiles that differ by end time, zone, or service version. For more information, see [Comparing profiles](https://cloud.google.com/profiler/docs/comparing-profiles).

## May 15, 2018

Feature

The new **Focus** filter lets you analyze the aggregate resource consumption of a specific function and the proportion of time spent in the function by different callers. For more information, see [Using the **Focus** Filter](https://cloud.google.com/profiler/docs/filtering-profiles#focus-filter).

## March 28, 2018

Feature

Stackdriver Profiler is released in Beta.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-02 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/release-notes/
title: App Engine flexible environment custom runtimes release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:15:06.341019+00:00
---

# App Engine flexible environment custom runtimes release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/flexible/resources)



Send feedback 

#  App Engine flexible environment custom runtimes release notes Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gaeflexiblecustomruntimes-release-notes.xml) directly. 

## September 29, 2026

Feature

App Engine permanently blocks insecure traffic with TLS version 1.1 and earlier. For `appspot.com` domains, this block occurs at the connection level. For custom domains, the connection might succeed, but the requests are blocked. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

## August 20, 2026

Feature

Starting from August 2026, to provide modern security patches and support for MySQL 8.4 and later, the App Engine flexible environment uses Cloud SQL Auth Proxy v2 as the built-in sidecar container for connections to Cloud SQL. To use the latest Cloud SQL Auth Proxy container immediately, restart your VMs or deploy a new version of your application.

## August 14, 2026

Feature

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

## June 29, 2026

Feature

Support for deploying your existing apps in the flexible environment to Cloud Run using the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the flexible environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-flexible-to-run).

## October 20, 2025

Feature

[Support for TLS version 1.2 and later](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls), along with a corresponding secure set of cipher suites, is in General Availability (GA).

## August 07, 2025

Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls) in the App Engine flexible environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

## March 18, 2025

Announcement

Container Registry is now [shut down](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown). We recommend that you use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) for storing and managing container images. By default, new deployments created after March 5, 2025, use Artifact Registry instead of Container Registry for storing application build images. For more information, see [Migrate App Engine container images to Artifact Registry](https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry).

## July 30, 2024

Feature

In the App Engine page in the Google Cloud console, you can now filter your existing App Engine versions by [runtime lifecycle stages](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle). After you apply this filter, the console displays a warning icon for App Engine versions that are approaching end of support, have reached end of support, are deprecated, and are decomissioned.

## July 12, 2024

Announcement

Deployments for new projects might be impacted from the following changes to org policies:

  * Starting in May 2024, Google Cloud enforces [secure-by-default organization policies](https://resource-manager/docs/secure-by-default-organizations) for all organization resources. This policy prevents App Engine from granting the `Editor` role to the App Engine default services accounts by default.
  * Starting in June 2024, Cloud Build has changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying versions for the first time may be using the default App Engine service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants%22) for deploying versions. 



If you are impacted by this change, you can do the following:

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).
  * Grant the [Editor](https://docs.cloud.google.com/appengine/docs/flexible/roles) role to the App Engine default service account.



## December 21, 2023

Change

A warning message now appears before you publish a container image to a public repository.

## August 07, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/appengine/docs/flexible/ingress-settings) now results in a `404` rather than `403` error code.

## March 24, 2023

Feature

You can now use `ssh` to log in to App Engine flexible environment instances that use only [internal IP addresses](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip).

## July 08, 2020

Feature

External HTTP(S) Load Balancing is now supported for App Engine via [Serverless network endpoint groups](https://load-balancing/docs/negs/setting-up-serverless-negs). Notably, this feature allows you to use [Cloud CDN](https://docs.cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

## March 13, 2020

Feature

App Engine is now available in the `asia-northeast3` region (Seoul).

## February 11, 2020

Feature

App Engine is changing the URLs that you use to send requests to your apps. URLs now include a region ID to help Google route your requests more efficiently and reliably. For example, an app can receive requests at https://**PROJECT_ID**.**REGION_ID**.r.appspot.com. This new URL is optional for existing apps and is provided for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region IDs. If we haven't updated your Google Cloud project yet, you won't see a region ID for your app. Since the ID is optional for existing apps, you don't need to update URLs or make other changes once the region ID is available for your existing apps.

## July 10, 2018

Feature

  * App Engine is now available in the `us-west2` region (Los Angeles).



## January 10, 2018

Feature

  * App Engine is now available in the `northamerica-northeast1` region (Montréal, Canada).



## March 28, 2017

Feature

  * The flexible environment is now available in the [`europe-west` region](https://docs.cloud.google.com/appengine/docs/locations).



## March 09, 2017

Feature

  * The [.NET core runtime](https://docs.cloud.google.com/appengine/docs/flexible/dotnet) for the App Engine flexible environment is now in Beta.



Feature

  * The App Engine flexible environment is now generally available (GA). You can run Node.js, Ruby, Python, Java, and Go applications with a [99.95% SLA](https://cloud.google.com/appengine/sla).



Feature

  * The [PHP 7 runtime](https://docs.cloud.google.com/appengine/docs/flexible/php) for the App Engine flexible environment is now in Beta.



## May 02, 2016

Feature

  * The [Ruby runtime](https://docs.cloud.google.com/appengine/docs/flexible/ruby) is now available for the App Engine flexible environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/appengine/docs/flexible/go/release-notes/
title: App Engine flexible environment for Go release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:52:54.221842+00:00
---

# App Engine flexible environment for Go release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/go/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/flexible/resources)



Send feedback 

#  App Engine flexible environment for Go release notes Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gaeflex-go-release-notes.xml) directly. 

## October 24, 2026

Security

The following runtime language contains important security updates:

  * [Go 1.24 and later](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go): `1.24.13`, `1.25.14`, `1.26.10`, `1.27.3`



The following stacks and their underlying operating system packages have also been updated:

  * `google-22`, `google-22-full`
  * `google-24`, `google-24-full`



Take immediate protective action by rebuilding and redeploying your resources with updated dependencies.

See [Security bulletins for Google Cloud](https://docs.cloud.google.com/support/bulletins) for more information.

## September 29, 2026

Feature

App Engine permanently blocks insecure traffic with TLS version 1.1 and earlier. For `appspot.com` domains, this block occurs at the connection level. For custom domains, the connection might succeed, but the requests are blocked. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

## September 01, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## August 20, 2026

Feature

Starting from August 2026, to provide modern security patches and support for MySQL 8.4 and later, the App Engine flexible environment uses Cloud SQL Auth Proxy v2 as the built-in sidecar container for connections to Cloud SQL. To use the latest Cloud SQL Auth Proxy container immediately, restart your VMs or deploy a new version of your application.

## August 19, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates align more closely with the [Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more information, see [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go).

## August 14, 2026

Feature

To improve security, starting in August 2026, App Engine opts your application into TLS version 1.2 and later. You can opt out until the end of August 2026. Starting in September 2026, App Engine might permanently block insecure traffic with TLS version 1.1 and earlier. For more information, see [Secure minimum TLS](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls).

## June 29, 2026

Feature

Support for deploying your existing apps in the flexible environment to Cloud Run using the `gcloud beta app migrate-to-run` command is in [Preview](https://cloud.google.com/products/#product-launch-stages). For more information, see [Deploy an App Engine app in the flexible environment to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-flexible-to-run).

## March 12, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 19, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## October 20, 2025

Feature

[Support for TLS version 1.2 and later](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls), along with a corresponding secure set of cipher suites, is in General Availability (GA).

## August 21, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## August 07, 2025

Feature

To increase security, starting in March 2025, support for Transport Layer Security (TLS) version 1.1 and earlier is deprecated. [Update your application settings](https://docs.cloud.google.com/appengine/docs/flexible/secure-minimum-tls) in the App Engine flexible environment to use TLS version 1.2 and later, along with a corresponding secure set of cipher suites (Preview).

## July 30, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages).

## July 15, 2025

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## March 18, 2025

Announcement

Container Registry is now [shut down](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown). We recommend that you use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) for storing and managing container images. By default, new deployments created after March 5, 2025, use Artifact Registry instead of Container Registry for storing application build images. For more information, see [Migrate App Engine container images to Artifact Registry](https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry).

## March 03, 2025

Feature

[Go 1.23](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now [ generally available](https://cloud.google.com/products/#product-launch-stages).

## November 19, 2024

Feature

[Go 1.23](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now available [in preview](https://cloud.google.com/products/#product-launch-stages).

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



## July 10, 2024

Announcement

Go version 1.19 and earlier have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#go). We recommend that you upgrade your app to use the [latest version of Go](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#newversions).

## March 26, 2024

Feature

[Go 1.22](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now [ generally available](https://cloud.google.com/products/#product-launch-stages). 

Starting in Go version 1.22 and later:

  * You can't use `go get` outside of a module in the legacy `GOPATH` mode (`GO111MODULE=off`).
  * Go recommends that you use a `go.mod` file for managing dependencies. 



For more information, see [Specify dependencies](https://docs.cloud.google.com/appengine/docs/standard/go/specifying-dependencies).

## February 26, 2024

Feature

[Go 1.22](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now available in [preview](https://cloud.google.com/products/#product-launch-stages).

## December 21, 2023

Change

A warning message now appears before you publish a container image to a public repository.

## September 08, 2023

Feature

[Go 1.21](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## August 14, 2023

Feature

[Go 1.21](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime) is now available in [preview](https://cloud.google.com/products/#product-launch-stages).

## August 07, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/appengine/docs/flexible/ingress-settings) now results in a `404` rather than `403` error code.

## April 28, 2023

Feature

You can now specify version "`1.20`" in the `runtime_version` setting of your `app.yaml` file. [Learn more](https://docs.cloud.google.com/appengine/docs/flexible/go/runtime#newversion).

## May 23, 2022

Feature

You can now disable external ephemeral IP addresses for App Engine Flex services. Read our documentation to [learn how](https://docs.cloud.google.com/appengine/docs/flexible/go/disable-external-ip). This feature is at the [Preview](https://cloud.google.com/products/#product-launch-stages) launch stage.

## May 18, 2022

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/go/user-managed-service-accounts) for each App Engine version during deployment is now [generally available](https://cloud.google.com/products/#general-availability).

## July 19, 2021

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/go/user-managed-service-accounts) for each App Engine version during deployment is now available in preview. This feature lets you grant different privileges to each version, based on the specific tasks it performs, and avoid granting more privileges than necessary.

## June 30, 2021

Change

Requests from internal services to the App Engine flexible environment no longer originate from `10.0.0.1`. The IP ranges are as follows: \- Cron requests from newly created or updated App Engine Cron jobs sent to the App Engine flexible environment now come from `0.1.0.2`. For Cron jobs created with older gcloud versions (earlier than 326.0.0), Cron requests will come from `0.1.0.1`. Previously, these requests only came from both `0.1.0.1` and `10.0.0.1`. \- For other Cloud Scheduler jobs and Cloud Tasks queues (including App Engine Task Queues), requests sent to the App Engine flexible environment now only come from `0.1.0.2`. Previously, these requests came from both `0.1.0.2` and `10.0.0.1`. \- For URL Fetch, requests sent to the App Engine flexible environment now only come from `0.1.0.40`. Previously, these requests came from both `0.1.0.40` and `10.0.0.1`.

For more information, see [Understanding the App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/go/understanding-firewalls).

## June 14, 2021

Feature

App Engine is now available in the `us-west1` (Oregon), `asia-southeast1` (Singapore), and `asia-east1` (Taiwan) regions.

## April 13, 2021

Feature

App Engine is now available in the `europe-central2` region (Warsaw).

## September 25, 2020

Feature

You can use [network ingress controls](https://docs.cloud.google.com/appengine/docs/flexible/go/application-security#ingress_controls) so your app only receives requests that are sent from your project's VPC or that are routed through the Cloud Load Balancing load balancer.

## July 08, 2020

Feature

External HTTP(S) Load Balancing is now supported for App Engine via [Serverless network endpoint groups](https://load-balancing/docs/negs/setting-up-serverless-negs). Notably, this feature allows you to use [Cloud CDN](https://docs.cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

## March 13, 2020

Feature

App Engine is now available in the `asia-northeast3` region (Seoul).

## March 06, 2020

Feature

App Engine is now available in the `us-west3 region` (Salt Lake City, Utah).

## February 11, 2020

Feature

App Engine is changing the URLs that you use to send requests to your apps. URLs now [include a region ID](https://docs.cloud.google.com/appengine/docs/flexible/go/how-requests-are-routed#region-id) to help Google route your requests more efficiently and reliably. For example, an app can receive requests at `https://PROJECT_ID.REGION_ID.r.appspot.com`. This new URL is optional for existing apps and is provided for all new apps.

To ensure a smooth transition, we are slowly updating App Engine to use region IDs. If we haven't updated your Google Cloud project yet, you won't see a region ID for your app. Since the ID is optional for existing apps, you don't need to update URLs or make other changes once the region ID is available for your existing apps.

## August 01, 2018

Feature

  * Support for Go 1.8 on App Engine is now [deprecated](https://docs.cloud.google.com/appengine/docs/deprecations).



Deprecated

  * New Go 1.6 and Go 1.8 app deployments will not be possible from November 1, 2018.



## July 10, 2018

Feature

  * App Engine is now available in the `us-west2` region (Los Angeles).



## December 14, 2017

Feature

  * Improved access control documentation around deploying apps with IAM roles and service accounts:

    * [Predefined App Engine roles](https://docs.cloud.google.com/appengine/docs/flexible/go/access-control#predefined_app_engine_roles)
    * [Deploying using IAM roles](https://docs.cloud.google.com/appengine/docs/flexible/go/granting-project-access#deploying_using_iam_roles)
    * [Require permissions](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#required_permissions)



## October 31, 2017

Feature

  * App Engine is now available in the `asia-south1` region (Mumbai, India).



## October 11, 2017

Feature

  * Announced general availability of [App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/go/creating-firewalls).



## October 02, 2017

Feature

  * For the App Engine flexible environment, all responses are now compressed with gzip by default once you redeploy your app. No changes need to be made to your `app.yaml` file.



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



## December 06, 2016

Change

  * New applications that have not been deployed in the flexible environment must specify `env: true` in the `app.yaml` file instead of `vm:true`. Applications that were previously deployed can continue to use `vm:true` but will need to switch to `env:true` in the future. For more details, see [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/go/upgrading).



## November 15, 2016

Feature

This release includes a few key new features:

  * Multi-zonal deployment support.
  * A modern networking stack with increased throughput.
  * Custom machine types.
  * Asia-Northeast1 region availability.



Feature

There is a new release of the App Engine flexible environment. To choose this environment, use `env:flex` instead of `vm:true` in your `app.yaml` configuration file. You can learn more about the details of this release by visiting the [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/go/upgrading).

Change

There are also a few breaking changes:

  * HTTP headers have been changed.
  * Environment variables have been changed.
  * There are multiple changes to the `app.yaml` schema.



For details and a full list of changes, visit the [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/go/upgrading).

Deprecated

This release also marks the deprecation of a few features:

  * The python-compat runtime.
  * The python27 runtime.
  * The java-compat runtime.
  * The jetty9-compat runtime.
  * The [Go App Engine package](https://github.com/golang/appengine) no longer works on the App Engine flexible environment. Instead, use the [`cloud.google.com/go/...` package](https://github.com/GoogleCloudPlatform/google-cloud-go).



## May 02, 2016

Feature

  * The [Ruby runtime](https://docs.cloud.google.com/appengine/docs/flexible/ruby) is now available for the App Engine flexible environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

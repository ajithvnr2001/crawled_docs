---
url: https://docs.cloud.google.com/appengine/docs/flexible/dotnet/release-notes/
title: App Engine flexible environment for .NET release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-06T05:52:54.796991+00:00
---

# App Engine flexible environment for .NET release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/dotnet/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/flexible/resources)



Send feedback 

#  App Engine flexible environment for .NET release notes Stay organized with collections  Save and categorize content based on your preferences. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gaeflex-net-release-notes.xml) directly. 

## October 24, 2026

Security

The following runtime language contains important security updates:

  * [.NET 6 and later](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#net): `6.0.428`, `8.0.415`, `10.0.100`



The following stacks and their underlying operating system packages have also been updated:

  * `google-22`, `google-22-full`
  * `google-24`, `google-24-full`



Take immediate protective action by rebuilding and redeploying your resources with updated dependencies.

See [Security bulletins for Google Cloud](https://docs.cloud.google.com/support/bulletins) for more information.

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

## February 18, 2026

Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime) is in [General Availability](https://cloud.google.com/products/#product-launch-stages).

## January 27, 2026

Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime) is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## January 10, 2024

Feature

[.NET 8](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## August 07, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/appengine/docs/flexible/ingress-settings) now results in a `404` rather than `403` error code.

## May 12, 2023

Feature

[.NET 6](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime) is now [generally available](https://cloud.google.com/products/#product-launch-stages). This version requires you to specify an operating system version in your `app.yaml` file. [Learn more](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime#newversions).

## April 28, 2023

Feature

[.NET 6](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime) is now available in [preview](https://cloud.google.com/products/#product-launch-stages). This version requires you to specify an operating system version in your `app.yaml` file. [Learn more](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime#newversions).

## March 24, 2023

Feature

You can now use `ssh` to log in to App Engine flexible environment instances that use only [internal IP addresses](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip).

## December 13, 2022

Feature

You can now use any configured [service account](https://docs.cloud.google.com/iam/docs/service-accounts) in your Cloud project as the [app-level default service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts), while creating and updating your App Engine applications.

## November 09, 2022

Feature

The option to set [IP mode to `internal`](https://cloud.google.com/appengine/docs/flexible/troubleshooter/connectivity-questions#virtual_machines_with_only_internal_ip_addresses_require) for App Engine flexible environment instances is now generally available.

## May 23, 2022

Feature

You can now disable external ephemeral IP addresses for App Engine Flex services. Read our documentation to [learn how](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/disable-external-ip). This feature is at the [Preview](https://cloud.google.com/products/#product-launch-stages) launch stage.

## May 18, 2022

Feature

Specifying a [user-managed service account](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/user-managed-service-accounts) for each App Engine version during deployment is now [generally available](https://cloud.google.com/products/#general-availability).

## March 04, 2019

Feature

[Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs) is now GA and can be used to set up scheduled units of work (cron jobs).

## October 22, 2018

Feature

  * App Engine is now available in the `asia-east2` region (Hong Kong).



## July 10, 2018

Feature

  * App Engine is now available in the `us-west2` region (Los Angeles).



## May 04, 2018

Feature

  * Applications in the App Engine flexible environment currently use a Debian 8 "Jessie" operating system. The Debian 8 "Jessie" OS will lose full support from the Debian maintainers in June 2018. In advance of this change, Google will migrate customers to an Ubuntu-based OS starting on May 30, 2018. To update your application to the Ubuntu 16.04 OS, re-deploy your application after May 30, 2018.



If for some reason you need to opt-out of this automatic upgrade, you can [pin your application to the old Debian 8 "Jessie" OS](https://docs.cloud.google.com/appengine/docs/deprecations/pin-app-to-debian).

## January 10, 2018

Feature

  * App Engine is now available in the `northamerica-northeast1` region (Montréal, Canada).bn `



## December 14, 2017

Feature

  * Improved access control documentation around deploying apps with IAM roles and service accounts:

    * [Predefined App Engine roles](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/access-control#predefined_app_engine_roles)
    * [Deploying using IAM roles](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/granting-project-access#deploying_using_iam_roles)
    * [Require permissions](https://docs.cloud.google.com/appengine/docs/admin-api/access-control#required_permissions)



## October 31, 2017

Feature

  * App Engine is now available in the `asia-south1` region (Mumbai, India).



## October 11, 2017

Feature

  * Announced general availability of [App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/creating-firewalls).



## October 05, 2017

Feature

  * .NET Core support is generally available on the App Engine flexible environment. Docker images are available for .NET Core 1.0, 1.1, and 2.0.



## October 02, 2017

Feature

  * For the App Engine flexible environment, all responses are now compressed with gzip by default once you redeploy your app. No changes need to be made to your `app.yaml` file.



## September 26, 2017

Feature

  * For the App Engine flexible environment, billing increments for instances are reduced from per-minute increments to per-second increments. Additionally, the minimum usage cost for instance resources is reduced from 10 minutes to 1 minute.



## September 18, 2017

Deprecated

Legacy health checks will no longer be available after September 30th, 2018.

Feature

  * [Updated health checks](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/reference/app-yaml#updated_health_checks) are now the default for new projects. To upgrade a project from legacy health checks, run the command `gcloud app update --split-health-checks`.



## September 13, 2017

Feature

  * You can now use managed certificates to add SSL to your custom domain. Once you map your custom domain to your application, App Engine provisions an SSL certificate automatically and handles renewing the certificate before it expires and revoking it if you remove the custom domain. Managed certificates are in beta. For more information, see [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/securing-custom-domains-with-ssl).



Feature

  * The `gcloud` commands and Admin API methods used to [map custom domains](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/mapping-custom-domains) are now generally available. This includes [`gcloud domains verify`](https://docs.cloud.google.com/sdk/gcloud/reference/domains) and [`apps.authorizedDomains.list`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list). However, if you want to use managed SSL certificates, use the beta commands and methods that are specified in [Securing Custom Domains with SSL](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/securing-custom-domains-with-ssl).



Feature

  * If you have an existing domain mapping and SSL certificate, then it continues to function as expected. You can also [upgrade to managed SSL certificates](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/securing-custom-domains-with-ssl#updating_to_managed_ssl_certificates).



## September 05, 2017

Feature

  * App Engine is now available in the `southamerica-east1` region (São Paulo, Brazil).



## August 23, 2017

Feature

  * Beta release of the [App Engine firewall](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/creating-firewalls).



## August 01, 2017

Feature

  * App Engine is now available in the `europe-west3` region (Frankfurt, Germany).



## July 18, 2017

Feature

  * App Engine is now available in the `australia-southeast1` region (Sydney, Australia).



## July 12, 2017

Feature

  * You can now use updated health checks, which allow you to use separate checks to confirm that your instance is running and ready to serve content. You must enable updated health checks, which are currently in Beta. For more information, see [Health checks](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/configuring-your-app-with-app-yaml#health_checks).



Change

  * If you use updated health checks, deployments will fail if your application does not reach a ready state.



## June 06, 2017

Feature

  * App Engine is now available in the `europe-west2` region (London).



Feature

  * You can now use the beta-level features in the Admin API and `gcloud` command-line tool to [create and manage your custom domains and SSL certificates](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/using-custom-domains-and-ssl) .



## May 09, 2017

Feature

  * App Engine is now available in the `us-east4` region (North Virginia).



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

Feature

  * New applications that have not been deployed in the flexible environment must specify `env: true` in the `app.yaml` file instead of `vm:true`. Applications that were previously deployed can continue to use `vm:true` but will need to switch to `env:true` in the future. For more details, see [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/python/upgrading).



## November 15, 2016

Feature

This release includes a few key new features:

  * Multi-zonal deployment support.
  * A modern networking stack with increased throughput.
  * Custom machine types.
  * Asia-Northeast1 region availability.



Feature

There is a new release of the App Engine flexible environment. To choose this environment, use `env:flex` instead of `vm:true` in your `app.yaml` configuration file. You can learn more about the details of this release by visiting the [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/python/upgrading).

Change

There are also a few breaking changes:

  * HTTP headers have been changed.
  * Environment variables have been changed.
  * There are multiple changes to the `app.yaml` schema.



For details and a full list of changes, visit the [upgrade guide](https://docs.cloud.google.com/appengine/docs/flexible/python/upgrading).

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



## March 24, 2016

Feature

  * App Engine Managed VMs is renamed to [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).



## February 03, 2016

Feature

  * Container construction choices for Managed VMs

The `gcloud preview app deploy` (and `mvn gcloud:deploy`) commands upload your artifacts to our servers and build a container to deploy your app to the Managed VM environment.

There are two mechanisms for building the container image remotely. The default behavior is to build the container on a transient Compute Engine Virtual Machine which has Docker installed. Alternatively, you can use the [Cloud Build](https://docs.cloud.google.com/build/docs) service, which is in Beta. To use the Cloud Build service, follow these steps:

    1. [Activate the Cloud Build API](https://support.google.com/cloud/answer/6158841) for your project.
    2. Use the command `gcloud config set app/use_cloud_build True`. This will cause all invocations of `gcloud preview app deploy` to use the service. To return to the default behavior, use the command `gcloud config set app/use_cloud_build False`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

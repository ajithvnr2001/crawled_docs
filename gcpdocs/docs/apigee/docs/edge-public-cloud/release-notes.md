---
url: https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes/
title: Apigee Edge for Public Cloud release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T10:51:32.914268+00:00
---

# Apigee Edge for Public Cloud release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Edge for Public Cloud release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Apigee Edge for Public Cloud, including updates to the Edge UI, SSO, Message Processor, and the integrated portal. This page also documents Edge Microgateway releases, starting with version 3.3.12. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

### What is a feed reader?

Really simple syndication (RSS) feed readers aggregate content from websites that you specify.

Feed reader notifications can be email-, browser-, desktop-, or mobile-based. Some readers are free, or have free versions, and some require a subscription.

A few examples:

  * [Feedly](https://feedly.com)
  * [Feedreader](https://feedreader.com)
  * [Feeder](https://feeder.co/)



More information on RSS:

  * [RSS](https://en.wikipedia.org/wiki/RSS)
  * [ Comparison of feed aggregators](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)



Close

See also:

  * [Release notes published before September 2026](https://docs.apigee.com/release/notes/apigee-release-notes)
  * [Earlier Edge Microgateway release notes](https://docs.apigee.com/release/notes/edge-microgateway-release-notes-0)
  * [Apigee Edge for Private Cloud release notes](https://docs.cloud.google.com/apigee/docs/edge-private-cloud/release-notes)
  * [Known issues](https://docs.apigee.com/release/known-issues)



rss_feed Subscribe: 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-edge-public-cloud-release-notes.xml) directly. 

## November 11, 2026

Announcement

On November 11, 2026, we began releasing Edge UI updates for Apigee Edge for Public Cloud.

Fixed

Bug ID | Component | Description  
---|---|---  
**392653797, 399185014** | Edge UI | Fixed an issue where navigating to the App Details or New App pages in organizations with a large number of API products experienced slowness or UI freezing during the initial page load. The Edge UI now fetches API products on demand when you open the **Add Product** dialog, improving initial page load performance.  
**576859695** | Edge UI | Fixed an issue in the Analytics Error Code Analysis dashboard where `504 Gateway Timeout` responses caused by target timeouts were excluded from the **Proxy errors** charts. Target timeout `504` responses are now counted under **Proxy errors**.  
**188163219** | Edge UI | Fixed a UI formatting issue in the Analytics Custom Reports list view so that dimensions display without overlapping.  
  
## November 05, 2026

Announcement

**Scheduled maintenance of Management/Control Plane for the Apigee Edge for Public Cloud on November 6, 2026.**

Scheduled maintenance of Management/Control Plane for the Apigee Edge for Public Cloud production will take place on Friday, November 6, 2026, from 9:00 PM PT to 10:00 PM PT (Saturday, November 7, 2026, from 5:00 AM UTC to 6:00 AM UTC). This maintenance follows the monthly maintenance window schedule documented in the [Apigee Edge release notes archive](https://docs.apigee.com/release/notes/apigee-release-notes).

During the scheduled maintenance window, the following services will be temporarily unavailable, and attempts to access them will return a `4xx` status code:

  * Management Services UI
  * Management Services APIs
  * Monetization Management APIs
  * New proxy deployments
  * DevPortal Service
  * Microgateway Services
  * Edge Query (Analytics Stats APIs)



Runtime API calls to deployed API proxies are unaffected. While access to analytics queries may be temporarily unavailable during the maintenance window, all analytics and metrics data from this period will be available once maintenance ends.

## November 04, 2026

Edge Microgateway 3.3.x

Announcement

Released Edge Microgateway 3.3.12.

Edge Microgateway 3.3.12 includes the following component versions:

Component | Version  
---|---  
[microgateway](https://github.com/apigee-internal/microgateway/releases) | 3.3.12  
[plugins](https://github.com/apigee/microgateway-plugins/releases) | 3.3.9  
[edgeauth](https://github.com/apigee/microgateway-edgeauth/releases) | 3.2.2  
  
To upgrade, install version 3.3.12 of the `edgemicro` npm package or pull the `gcr.io/apigee-microgateway/edgemicro:3.3.12` Docker image. For the npm upgrade steps, see [Upgrading Edge Microgateway](https://docs.apigee.com/api-platform/microgateway/3.3.x/operation-and-configuration-reference-edge-microgateway#upgradingedgemicrogateway). For earlier Edge Microgateway releases, see [Edge Microgateway release notes](https://docs.apigee.com/release/notes/edge-microgateway-release-notes-0).

Edge Microgateway 3.3.x

Breaking

Removed support for Node.js 20 from Edge Microgateway. Use Node.js 22, 24, or 26 instead.

Edge Microgateway 3.3.12 supports only Node.js 22, 24, and 26. Support for Node.js 26 is new in this release. Before you upgrade an npm installation of Edge Microgateway to 3.3.12, upgrade the Node.js runtime on each host to version 22, 24, or 26. The 3.3.12 Docker image is built on Node.js 24, so Docker deployments need no action for this change. For supported versions, see [Supported software and supported versions](https://docs.apigee.com/release/supported-software#apigeeedgemicrogateway).

Edge Microgateway 3.3.x

Breaking

Removed the `npm` and `npx` command-line tools from the Edge Microgateway Docker image. Install custom plugin dependencies before you add the plugins to the container.

Starting with version 3.3.12, the Edge Microgateway Docker image doesn't include `npm` or `npx`, and commands that run either tool inside the container fail. The change doesn't affect how Edge Microgateway runs. If your custom plugins have npm dependencies, run `npm install` in each plugin directory before you add the plugins to the container, so that each plugin's `node_modules` directory is included. For the steps, see [Adding a custom plugin](https://docs.apigee.com/api-platform/microgateway/3.3.x/docker#adding_a_custom_plugin). This change doesn't affect npm installations of Edge Microgateway.

Edge Microgateway 3.3.x

Security

Fixed multiple security vulnerabilities in Edge Microgateway. Upgrade to Edge Microgateway 3.3.12.

Edge Microgateway 3.3.12 fixes the following vulnerabilities:

  * [CVE-2026-12590](https://nvd.nist.gov/vuln/detail/CVE-2026-12590)
  * [CVE-2026-14257](https://nvd.nist.gov/vuln/detail/CVE-2026-14257)
  * [CVE-2026-45819](https://nvd.nist.gov/vuln/detail/CVE-2026-45819)
  * [CVE-2026-54272](https://nvd.nist.gov/vuln/detail/CVE-2026-54272)
  * [CVE-2026-59870](https://nvd.nist.gov/vuln/detail/CVE-2026-59870)
  * [CVE-2026-69152](https://nvd.nist.gov/vuln/detail/CVE-2026-69152)
  * [CVE-2026-69192](https://nvd.nist.gov/vuln/detail/CVE-2026-69192)
  * [CVE-2026-69198](https://nvd.nist.gov/vuln/detail/CVE-2026-69198)
  * [CVE-2026-73088](https://nvd.nist.gov/vuln/detail/CVE-2026-73088)
  * [CVE-2026-73089](https://nvd.nist.gov/vuln/detail/CVE-2026-73089)
  * [CVE-2026-82417](https://nvd.nist.gov/vuln/detail/CVE-2026-82417)
  * [CVE-2026-82562](https://nvd.nist.gov/vuln/detail/CVE-2026-82562)
  * [CVE-2026-84375](https://nvd.nist.gov/vuln/detail/CVE-2026-84375)
  * [CVE-2026-87018](https://nvd.nist.gov/vuln/detail/CVE-2026-87018)
  * [CVE-2026-101910](https://nvd.nist.gov/vuln/detail/CVE-2026-101910)
  * [CVE-2026-101911](https://nvd.nist.gov/vuln/detail/CVE-2026-101911)
  * [CVE-2026-101912](https://nvd.nist.gov/vuln/detail/CVE-2026-101912)
  * [CVE-2026-101913](https://nvd.nist.gov/vuln/detail/CVE-2026-101913)
  * [CVE-2026-102276](https://nvd.nist.gov/vuln/detail/CVE-2026-102276)
  * [CVE-2026-102277](https://nvd.nist.gov/vuln/detail/CVE-2026-102277)
  * [CVE-2026-102278](https://nvd.nist.gov/vuln/detail/CVE-2026-102278)
  * [CVE-2026-109383](https://nvd.nist.gov/vuln/detail/CVE-2026-109383)
  * [CVE-2026-109869](https://nvd.nist.gov/vuln/detail/CVE-2026-109869)
  * [CVE-2026-109924](https://nvd.nist.gov/vuln/detail/CVE-2026-109924)
  * [CVE-2026-109932](https://nvd.nist.gov/vuln/detail/CVE-2026-109932)
  * [CVE-2026-110816](https://nvd.nist.gov/vuln/detail/CVE-2026-110816)
  * [CVE-2026-111181](https://nvd.nist.gov/vuln/detail/CVE-2026-111181)
  * [CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497)
  * [CVE-2026-111997](https://nvd.nist.gov/vuln/detail/CVE-2026-111997)
  * [CVE-2026-115897](https://nvd.nist.gov/vuln/detail/CVE-2026-115897)



The Edge Microgateway 3.3.12 Docker image is built on `node:24.22.1-trixie-slim`, which includes the Node.js fix for CVE-2026-111497. For npm installations of Edge Microgateway, upgrading the `edgemicro` package doesn't fix CVE-2026-111497. You must also upgrade the Node.js runtime on each host to one of the following versions, or to a later version in the same release line:

Node.js release line | Fixed version  
---|---  
22.x | 22.23.4  
24.x | 24.22.1  
26.x | 26.12.1  
  
## October 15, 2026

Announcement

On October 15, 2026, we began releasing Single Sign-On (SSO) updates for Apigee Edge for Public Cloud.

Fixed

Bug ID | Component | Description  
---|---|---  
**560310696** | SSO | Fixed an issue where the Portal SSO endpoint inadvertently accepted deprecated TLS 1.1 connections. The endpoint now strictly enforces TLS 1.2+.  
  
## October 05, 2026

Security

**Security fixes for the integrated portal and API specs in the Apigee Edge management UIs.**

The Apigee Edge UIs for managing integrated portals and API specs were updated to patch vulnerabilities in underlying libraries and serving components. Functionality is unchanged, but some pages might show minor styling differences.

## September 02, 2026

Announcement

Apigee Edge for Public Cloud release notes are now published on Google Cloud documentation.

Release notes for Apigee Edge for Public Cloud, including its Edge UI, SSO, Message Processor, and integrated portal components, are published on the [Apigee Edge for Public Cloud release notes](https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes) page from September 2026 onward. You can [subscribe](https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes#sub) to that page with a feed reader to be notified when a new release is published.

Release notes published before September 2026 remain available in the [Apigee Edge release notes archive](https://docs.apigee.com/release/notes/apigee-release-notes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/docs/starter-tier/
title: Starter Tier overview \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T05:54:15.714885+00:00
---

# Starter Tier overview  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/starter-tier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Starter Tier overview Stay organized with collections  Save and categorize content based on your preferences. 

Starter Tier provides a no-cost, _Google-managed_ project that lets you build and deploy web apps and use select Google Cloud and Google products. If you sign in with an eligible Google Account, Google provisions a Starter Tier project on your behalf without requiring a payment method or Cloud Billing account.

This document explains how Starter Tier projects work, who is eligible, which Starter Tier services and connected services you can use, and how to upgrade your project.

## How Starter Tier projects work

If you're eligible, Google automatically provisions your resources in a _Google-managed_ Google Cloud project when you use a product or tool that supports Starter Tier. This project is called a Starter Tier project. Google manages the project and its underlying infrastructure on your behalf, so you can build and deploy apps or use certain Google products without providing billing information.

Because Google manages the underlying infrastructure, a Starter Tier project requires no manual setup and differs from _user-managed_ Google Cloud projects in the following ways:

  * **No Cloud Billing account or trial period:** You don't need to provide a payment method or set up a Cloud Billing account. A Starter Tier project has no fixed expiration period. If a service reaches its no-cost quota limit, usage pauses until the quota resets or you upgrade your project.
  * **Preconfigured project and usage limits:** Google limits each eligible Google Account to one Starter Tier project. All Starter Tier services and connected services that you use share the same project, and you can't manually create additional Starter Tier projects. Within a Starter Tier project, Google enforces the following configurations and limits until you upgrade your project:

    * **Regions and organization policies:** Google restricts regional resources to a single supported region and enforces organization policies that limit advanced configurations and unsupported features.
    * **Service quotas:** Services run within fixed no-cost limits on deployed apps, compute instances, storage, and requests.
    * **API enablements:** Only the APIs required for Starter Tier services and connected services are pre-enabled. You can't enable other Google Cloud APIs.
    * **Access control:** Google manages [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) permissions on the project. You can view and configure your supported resources, logs, and metrics, but you can't modify project IAM roles or create service accounts.
  * **Separate Terms of Service:** Your Starter Tier resources aren't standard Google Cloud services and aren't governed by the Google Cloud Terms of Service. Instead, Starter Tier services are governed by the [Starter Tier Additional Terms of Service](https://cloud.google.com/terms/starter-tier-additional-terms-of-service). Using Firebase services requires accepting the [Firebase Terms of Service](https://firebase.google.com/terms) in addition to the Starter Tier Additional Terms of Service. By contrast, connected services aren't covered by the Starter Tier Additional Terms of Service and are governed _only_ by their own Terms of Service.




## Starter Tier eligibility

Starter Tier is available to individual [Google Accounts](https://myaccount.google.com/) that meet all of the following criteria:

  * **Personal Google Account:** Your account isn't associated with a Google Workspace organization. Accounts in paid or free Google Workspace, Google Workspace for Education, or Google Workspace for Nonprofits aren't eligible.
  * **No paid Cloud Billing history:** Your account doesn't have an active or prior paid Cloud Billing account.
  * **Account activity and supported location:** Your account has sufficient account activity and is located in a supported territory.



### What happens if your account isn't eligible

If your account doesn't qualify for Starter Tier, you can still use the services listed in Starter Tier services and Connected services in a _user-managed_ Google Cloud project:

  * **Services that don't require billing:** You can use many services in a user-managed project within their no-cost limits without a Cloud Billing account, such as Firebase Authentication, Firestore, and Google Workspace APIs.
  * **Services that require billing:** To use services that require a Cloud Billing account in a user-managed project, such as deploying a live web app to Cloud Run or provisioning a Cloud SQL for PostgreSQL (developer edition) instance, you must [set up or link a Cloud Billing account](https://docs.cloud.google.com/billing/docs/in-product-billing-setup). Both Cloud Run and Cloud SQL for PostgreSQL (developer edition) include [monthly no-cost usage limits](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier-usage-limits) on eligible user-managed Google Cloud projects.



## Starter Tier services

You can use a Starter Tier project to build and deploy full-stack web apps from [Google AI Studio](https://aistudio.google.com/apps) with a curated set of Google Cloud and Firebase services. Your apps can also integrate with connected services governed only by their own Terms of Service. For step-by-step deployment instructions and project limits, see [Deploy from Google AI Studio](https://aistudio.google.com/docs/aistudio-deploying).

The following table describes the Starter Tier services (offered with limited functionality and quotas) governed by the [Starter Tier Additional Terms of Service](https://cloud.google.com/terms/starter-tier-additional-terms-of-service):

Service | Use case  
---|---  
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) |  Host your live web app and backend from your code, with no servers to manage and automatic scaling when traffic grows or drops to zero.  
[Firebase Authentication](https://firebase.google.com/docs/ai-assistance/ai-studio-integration) |  Add user sign-in and authentication to your app with Google Sign-In, email and password, or anonymous authentication.  
[Firestore](https://firebase.google.com/docs/ai-assistance/ai-studio-integration#understand-shared-quota) |  Store and sync your app's data in a NoSQL document database with automated auditing of security rules to help keep your app's data secure.  
[Cloud SQL for PostgreSQL (developer edition)](https://docs.cloud.google.com/sql/docs/postgres/ai-assisted-coding-and-cloud-sql) |  Provision a relational PostgreSQL database that automatically pauses and scales to zero when there are no active connections. For details on scale-to-zero behavior and pricing after upgrading, see [Starter Tier and pricing](https://docs.cloud.google.com/sql/docs/postgres/ai-assisted-coding-and-cloud-sql#starter-tier-and-pricing).  
  
To use Firebase services and manage them in the [Firebase console](https://console.firebase.google.com/), you must accept the [Firebase Terms of Service](https://firebase.google.com/terms) in addition to the Starter Tier Additional Terms of Service.

## Connected services

Your Starter Tier project can also connect to external Google APIs and services. Connected services aren't Starter Tier services and aren't covered by the Starter Tier Additional Terms of Service.

The following table describes the connected services you can use with your Starter Tier project (offered with limited functionality and quotas), each governed only by its own Terms of Service:

Service | Use case  
---|---  
[Google Maps Platform](https://developers.google.com/maps/ai/ai-studio) |  Add interactive maps, place search, address lookup, and directions to location-aware apps at no cost by using auto-provisioned Maps Demo Keys. Usage is governed by the [Maps Demo Project Terms of Service](https://cloud.google.com/terms/maps-platform/demo-project-terms).  
[Google Workspace APIs](https://developers.google.com/workspace/guides/get-started) |  Connect your web app to a user's services, such as Google Drive, Google Docs, Google Sheets, Google Slides, Google Calendar, Gmail, Google Forms, Google Tasks, and Google Picker, with built-in Google sign-in permissions. Usage is governed by the [Google APIs Terms of Service](https://developers.google.com/terms), the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), and any applicable [additional terms for Google Workspace APIs](https://developers.google.com/workspace/terms).  
  
## Upgrade your Starter Tier project

After you've tried services in your Starter Tier project, you might need higher quotas, more compute resources, custom domains, additional regions, or access to other Google Cloud services. To unlock these capabilities, you can upgrade your _Google-managed_ Starter Tier project to a _user-managed_ Google Cloud project.

Upgrading converts your Starter Tier project in place, so you don't need to create a new project or manually migrate your resources, databases, API keys, or web app URLs.

### Where to initiate an upgrade

You can initiate a one-step upgrade from Google AI Studio, the [Firebase console](https://console.firebase.google.com/), or the [Google Cloud console](https://console.cloud.google.com/). To upgrade and convert your Starter Tier project to a user-managed Google Cloud project, you must accept the Google Cloud Terms of Service and link or create a [Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account) by using [in-product Cloud Billing setup](https://docs.cloud.google.com/billing/docs/in-product-billing-setup).

### What happens when you upgrade

During the upgrade process, your project transitions in place to a _user-managed_ Google Cloud project:

  * Your running apps experience no downtime.
  * Your app state, databases, API keys, and web app URLs are preserved.
  * You gain full [IAM](https://docs.cloud.google.com/iam/docs/overview) control and ownership of the project.
  * You can enable any Google Cloud API.
  * If you're a first-time Google Cloud user, you might qualify for the $300 [Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features) credit or an in-product [welcome credit](https://docs.cloud.google.com/billing/docs/in-product-billing-setup#welcome-credits), as well as monthly [Free Tier](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier) usage limits.



After you upgrade to a user-managed project, your resources are billed at standard rates against your linked Cloud Billing account. The upgraded project is governed by the [Google Cloud Terms of Service](https://cloud.google.com/terms).

**Note:** If your Starter Tier project includes a Firestore database, linking a Cloud Billing account doesn't automatically remove the daily quota cap. For instructions on how to remove this cap, see [Add billing to get more Firestore quota](https://firebase.google.com/docs/ai-assistance/ai-studio-integration#add-billing).

## What's next

  * [Deploy from Google AI Studio](https://aistudio.google.com/docs/aistudio-deploying)
  * [Learn about the in-product Cloud Billing setup](https://docs.cloud.google.com/billing/docs/in-product-billing-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

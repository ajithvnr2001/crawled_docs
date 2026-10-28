---
url: https://docs.cloud.google.com/appengine/docs/standard/service-agent/
title: Google-managed service agent \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:49:55.293974+00:00
---

# Google-managed service agent  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/service-agent/

[ Skip to main content ](https://docs.cloud.google.com/appengine/docs/standard/service-agent/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/appengine/docs/standard/service-agent/)
  * [Deutsch](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=de)
  * [Español](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=es-419)
  * [Français](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=id)
  * [Italiano](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=it)
  * [Português](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=ja)
  * [한국어](https://docs.cloud.google.com/appengine/docs/standard/service-agent/?hl=ko)

Sign in
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/serverless-color.svg) ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Verify the service agent](https://docs.cloud.google.com/appengine/docs/standard/service-agent/#verify_the_service_agent)
  * [Restore required role for the service agent](https://docs.cloud.google.com/appengine/docs/standard/service-agent/#restore_required_role_for_the_service_agent)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)


Was this helpful?
Send feedback 
#  Google-managed service agent Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Verify the service agent](https://docs.cloud.google.com/appengine/docs/standard/service-agent/#verify_the_service_agent)
  * [Restore required role for the service agent](https://docs.cloud.google.com/appengine/docs/standard/service-agent/#restore_required_role_for_the_service_agent)


App Engine includes a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) named _App Engine standard environment Service Agent_ . This service agent enables your services to act on your behalf when accessing other Google Cloud resources. It is essential to keep the service agent unmodified.
Note that the service agent is not listed on the **Service Accounts** page in the Google Cloud console and is unrelated to the [App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/default-service-account).
The service agent for your Google Cloud project is automatically created after you deploy your first service—for example, after you run the `gcloud app deploy` command for the first time to deploy an app in the standard environment.
The service agent uses the predefined IAM role [App Engine standard environment Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent), which includes a set of permissions needed by App Engine to manage your apps. This role is granted to the service agent automatically when the service agent is created.
For example, the permissions allow your Google Cloud project to use the Blobstore API, or to obtain an access token that your App Engine instances use to access other Google Cloud resources, such as a Cloud Storage bucket.
**Important restrictions** :
  * Do not revoke the roles that are granted to the service agent.
  * Do not grant the related [App Engine standard environment Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/appengine#appengine.serviceAgent) to any other account. Note that the permissions in this role can change without notice.


## Verify the service agent
To verify that the service agent has its required role in your Google Cloud project, perform the following steps:
  1. In the Google Cloud console, go to the **Permissions** page.
[Go to Permissions](https://console.cloud.google.com/iam-admin/iam)
  2. In the upper-right corner of the **Permissions** page, select the **Include Google-provided role grants** checkbox.
  3. In the **Principals** list, locate the service agent with the following ID:  
`service-PROJECT_NUMBER@gcp-gae-service.iam.gserviceaccount.com`. 
  4. Verify that the service agent has been granted the **App Engine standard environment Service Agent** role. 


## Restore required role for the service agent
If you accidentally remove the required **App Engine standard environment Service Agent** role binding for the service agent from your Google Cloud project, restore it by performing the following steps:
  1. In the Google Cloud console, go to the **Permissions** page.
[Go to Permissions](https://console.cloud.google.com/iam-admin/iam)
  2. Click **Add**.
  3. Enter the service agent ID in the following format:  
`service-PROJECT_NUMBER@gcp-gae-service.iam.gserviceaccount.com`.
  4. Select the **App Engine standard environment Service Agent** role. 
  5. Click **Save**.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

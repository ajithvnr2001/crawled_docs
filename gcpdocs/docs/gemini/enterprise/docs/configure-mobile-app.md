---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/
title: Configure the mobile app \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:17:11.223625+00:00
---

# Configure the mobile app  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/

[ Skip to main content ](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/)
  * [Deutsch](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini%2Fenterprise%2Fdocs%2Fconfigure-mobile-app%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/gemini-spark-blue-192px.svg) ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#overview)
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#before-you-begin)
  * [Use a Mobile Device Management (MDM) solution](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#mdm-solution)
    * [Configure citation browser preferences](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#citation-browser-preferences-mdm)
  * [Enable a QR code on the web app homepage](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#enable-qr-code)
  * [Generate an access link](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#generate-access-link)
    * [Configure citation browser preferences](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#citation-browser-preferences-link)


**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)


Was this helpful?
Send feedback 
#  Configure the mobile app Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#overview)
  * [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#before-you-begin)
  * [Use a Mobile Device Management (MDM) solution](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#mdm-solution)
    * [Configure citation browser preferences](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#citation-browser-preferences-mdm)
  * [Enable a QR code on the web app homepage](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#enable-qr-code)
  * [Generate an access link](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#generate-access-link)
    * [Configure citation browser preferences](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#citation-browser-preferences-link)


This page explains how to configure the Gemini Enterprise mobile app on user devices. Gemini Enterprise app administrator can choose to configure access for users using one of three available methods.
## Overview
As a Gemini Enterprise administrator, you can configure the mobile app for users with one of three methods:
  * You can [use a Mobile Device Management (MDM) solution](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#mdm-solution) to remotely install and configure the app on user devices. MDM solutions allow admins to complete set up steps prior to delivering apps to users.
  * You can [enable a QR code](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#enable-qr-code) within the Gemini Enterprise web app. Users can then configure the mobile app by scanning this QR code. QR codes can simplify the distribution of access to users and can be used in addition to MDM solutions.
  * You can [generate an access link](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#generate-access-link) and distribute it to users, which lets them configure the app by opening the link on their mobile devices.


The following sections describe the steps required by each method.
## Before you begin
Before you configure the app for users, set up an identity provider for your Gemini Enterprise organization. The Gemini Enterprise mobile app supports the use of Google Identity and third-party identity providers. For more information, see [Configure identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).
## Use a Mobile Device Management (MDM) solution
The Gemini Enterprise administrator panel provides an app URL that contains the parameters required to configure the mobile app in your MDM solution. These parameters map directly to `AppConfig` parameters in the **AppConfig standard** and can be used to configure the app, and enforce security policies.
The following steps use Google Endpoint Management (GEM) as an example of configuring an MDM, but the `AppConfig` parameters should be applicable to other MDM solutions. These steps require access to your MDM administrator console. If you don't have access, contact your organization administrator for next steps.
To configure the app for users in the GEM MDM management solution:
  1. In the Google Cloud console, go to the Gemini Enterprise page.
[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)
  2. Click your app. The **Overview** page displays.
  3. Click **Copy URL** to copy the mobile link. The format of the mobile link differs based on your identity provider.
[ Google Identity ](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#google-identity)[ Third-party identity provider ](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#third-party-identity-provider) More
If your Gemini Enterprise app uses Google as an identity provider, the mobile app URL looks like this:

```
https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global

```

If your Gemini Enterprise app uses a third-party identity provider, the mobile app URL looks like this:

```
https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global&idp=locations/global/workforcePools/my-pool/providers/my-provider

```

  4. Extract the parameters from the app URL, and use them to fill in the app configuration in your MDM administrator console:
[ Google Identity ](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#google-identity)[ Third-party identity provider ](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#third-party-identity-provider) More  
| **Deeplink parameter**  | **MDM configuration key**  | **MDM configuration name**  | **Example value**  |  
| --- | --- | --- | --- |  
| `cid`  | `config_id`  | Configuration ID  | `123`  |  
| `cid_location`  | `location`  | Location  | `global`  |  
Leave all other fields empty.
For example, the following XML configures an iOS application in GEM:

```
<dict>
   <key>config_id</key>
   <string>123</string>
   <key>location</key>
   <string>global</string>
</dict>

```
  
| **Deeplink parameter**  | **MDM configuration key**  | **MDM configuration name**  | **Example value**  |  
| --- | --- | --- | --- |  
| `cid`  | `config_id`  | Configuration ID  | `123`  |  
| `cid_location`  | `location`  | Location  | `global`  |  
| `idp`  | `identity_provider`  | Identity Provider  | `locations/global/workforcePools/my-pool/providers/my-provider`  |  
| `tenant_id`  | `tenant_id`  | Tenant ID (Deprecated, leave empty)  |   |  
| `client_id`  | `client_id`  | Client ID (Deprecated, leave empty)  |   |  
| `project_id`  | `project_id`  | Project ID (Deprecated, leave empty)  |   |  


### Configure citation browser preferences
Gemini Enterprise administrators can use MDM configuration keys to specify how citations and web pages open from Gemini Enterprise mobile sessions.
  * **Open citations in the default browser**
To open citations in the system's default browser using MDM, set the following MDM configuration key:

```
url_launch_mode = external_browser

```

  * **Open citations in a specific browser**
To force citations to open in a specific browser using MDM, set an additional MDM configuration key:

```
url_launch_mode = external_browser, preferred_browser = chrome (or edge, or firefox)

```



## Enable a QR code on the web app homepage
As a Gemini Enterprise administrator, you can display a QR code on the web app homepage, which allows users to configure the mobile app on their devices by scanning the QR code using their device's camera. This serves as a simpler way to distribute the access link to users.
To manage the configuration QR code visibility:
  1. In the Google Cloud console, go to the Gemini Enterprise page.
[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)
  2. Click the name of the app that you want to configure.
  3. Click **Configurations** and then click the **Feature Management** tab.
  4. Turn on or turn off the **Enable mobile app access** toggle to display or hide the QR code on the web app user's home page.


After the QR code is enabled, users can scan the QR code displayed on their Gemini Enterprise web app using their mobile device to configure and connect the mobile app.
To view the QR code on the web app to set up the mobile app:
  1. Open your Gemini Enterprise web app.
  2. Click **Settings & help**.
  3. Click **Mobile login**.
  4. Scan the QR code with your mobile device to sign in to the Gemini Enterprise mobile app.


## Generate an access link
To generate the access link for distribution to Gemini Enterprise mobile app users, do the following:
  1. In the Google Cloud console, go to the Gemini Enterprise page.
[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)
  2. Click your app. The **Overview** page displays.
  3. Click **Copy URL** to copy the mobile link. You can then distribute the link to users. The format of the mobile link differs based on your identity provider.
[ Google Identity ](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#google-identity)[ Third-party identity provider ](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app/#third-party-identity-provider) More
If your Gemini Enterprise uses Google as an identity provider, the mobile app URL looks like this:

```
https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global

```

If your Gemini Enterprise uses a third-party identity provider, the mobile app URL looks like this:

```
https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global&idp=locations/global/workforcePools/my-pool/providers/my-provider

```



### Configure citation browser preferences
Gemini Enterprise administrators can use access link parameters to specify how citations and web pages open from Gemini Enterprise mobile sessions.
  * **Open citations in the default browser**
To open citations in the system's default browser with an access link, pass the following parameter in the URL:

```
url_launch_mode=external_browser

```

  * **Open citations in a specific browser**
To force citations to open in a specific browser with an access link, pass set an additional parameter in the URL:

```
url_launch_mode=external_browser, preferred_browser=chrome (or edge, or firefox)

```

For example:

```
https://vertexaisearch.cloud.google.com/mobile?cid=123&cid_location=global&url_launch_mode=external_browser&preferred_browser=chrome

```



Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

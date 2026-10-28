---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/
title: Demote media recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:00:44.318529+00:00
---

# Demote media recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/

[ Skip to main content ](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/)
  * [Deutsch](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=de)
  * [Español](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=es-419)
  * [Français](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=id)
  * [Italiano](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=it)
  * [Português](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=ja)
  * [한국어](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg) ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Demote based on viewer data](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/#demote-viewer-data)
  * [Demote based on content age](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/#demote-content-age)


**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)


Send feedback 
#  Demote media recommendations Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Demote based on viewer data](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/#demote-viewer-data)
  * [Demote based on content age](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/#demote-content-age)


When you use media recommendations, you can demote recommendations based on viewer data or content age. Recommendations that meet the demotion criteria that you specify are demoted to the bottom of the results list. This feature is available only for media recommendations, not for custom search and recommendations.
Demotion is set on the serving config level. You can have multiple serving configs per media recommendations app, each with a different demotion setting. For more information about serving configs, see [Create and manage serving configs](https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs).
## Demote based on viewer data
You can demote recommendations based on how an end user has recently interacted with the recommended content.
If your recommended content has a detail page, then you can demote it if the user has recently viewed it. If your content is playable media, then you can demote it depending on the amount of time the user played it or the percentage of the content that the user played.
To demote recommendations based on viewer data:
  1. In the Google Cloud console, go to the **AI Applications** page.
[AI Applications](https://console.cloud.google.com/gen-app-builder/start)
  2. Click the name of the app that you want to configure recommendations for.
  3. Go to the **Configurations** > **Control** tab.
  4. If you have more than one serving config, select the serving config that you plan to set demotion for.
  5. In the **Recommendation demotion** section, turn on the **Demote recommendations based on viewer data** toggle to see the available demotion options.
  6. Select your demotion option and, if prompted, enter a threshold value for when to trigger demotion.
  7. Click **Save and publish**.


## Demote based on content age
You can demote playable content based on its age. You set the age threshold in days, and any content that reaches that age is demoted to the bottom of the results list.
To demote recommendations based on content age:
  1. In the Google Cloud console, go to the **AI Applications** page.
[AI Applications](https://console.cloud.google.com/gen-app-builder/start)
  2. Click the name of the app that you want to configure recommendations for.
  3. Go to the **Configurations** > **Control** tab.
  4. If you have more than one serving config, select the serving config that you plan to set demotion for.
  5. In the **Recommendation demotion** section, turn on the **Demote recommendations based on content age** toggle.
  6. Enter a content age threshold value for when to trigger demotion.
  7. Click **Save and publish**.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

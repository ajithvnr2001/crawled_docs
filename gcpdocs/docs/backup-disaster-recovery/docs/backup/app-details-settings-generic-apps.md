---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/
title: Configure application details and settings for generic applications in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:09:41.089834+00:00
---

# Configure application details and settings for generic applications in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/

[ Skip to main content ](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/)
  * [Deutsch](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=de)
  * [Español](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=es-419)
  * [Français](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=id)
  * [Italiano](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=it)
  * [Português](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=ja)
  * [한국어](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/app-details-settings-generic-apps/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/operations-color.svg) ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)


Send feedback 
#  Configure application details and settings for generic applications in the appliance management console Stay organized with collections  Save and categorize content based on your preferences.
From the appliance management console **Application Details & Settings** page, you can modify application-specific settings for capturing **Generic Apps** —other LVM (logical volume manager) applications not listed in the appliance management console. Application settings may be useful or required in certain circumstances. After you configure your application settings, click **Save Changes**.
The following is a list of application settings with descriptions. 
  * **Backup and DR agent options** : Leave Backup and DR agent options blank unless you are working with support.
  * **Freeze and Thaw Script Name** : Location of the custom script on the host. Scripts are called to freeze or unfreeze an application before a job.
  * **Percentage of Reserve Space in Volume Group** : This is the space logical volume manager consumes to track changes to production volumes when an logical volume manager snapshot is in effect. By default it is 20%.
  * **Use Buffered Copy** : Select from **Yes** or **No** —default.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

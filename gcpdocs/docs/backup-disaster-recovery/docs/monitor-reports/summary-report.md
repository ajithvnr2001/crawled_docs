---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/
title: Summary reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:00:01.324124+00:00
---

# Summary reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/

[ Skip to main content ](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/)
  * [Deutsch](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=de)
  * [Español](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=es-419)
  * [Français](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=id)
  * [Italiano](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=it)
  * [Português](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=ja)
  * [한국어](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/operations-color.svg) ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Appliance health dashboard](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#dashboard)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions)
  * [Resource consumption by appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#app-consum)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions_2)
  * [Resource consumption by application](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#consum-app)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions_3)
  * [Resource consumption by policy templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#consum-tem)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions_4)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)


Send feedback 
#  Summary reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Appliance health dashboard](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#dashboard)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions)
  * [Resource consumption by appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#app-consum)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions_2)
  * [Resource consumption by application](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#consum-app)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions_3)
  * [Resource consumption by policy templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#consum-tem)
    * [Column descriptions](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#column_descriptions_4)


The summary reports provide the daily overall status of an appliance. It is a combination of several sub-reports.
Summary reports include:
  * [Appliance health Dashboard](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#dashboard)
  * [Resource consumption by appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#app-consum)
  * [Resource consumption by application](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#consum-app)
  * [Resource consumption by policy template](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/summary-report/#consum-tem)


## Appliance health dashboard
This report shows the key attributes and resource constraints for each appliance, with colors to indicate resources (disk pools, vDisks, elapsed time since last data sync) that are approaching or exceeding their limits. A yellow color indicates a warning threshold and a red color indicates a critical level. The percentage used column (% Used) for snapshot pools is the ratio of usage and capacity of all the snapshot pools on the appliance.
### Column descriptions
  * **Appliance.** Name of the appliance.
  * **Last Sync Elapsed (hr:min).** Number of hours since the last successful data sync.
  * **Software Version.** Version of the appliance.
  * **Protected Data (TB).** **Protected Data Licenses** consumed by the appliance in tebibytes, along with a trend line.
**Snapshot Pools, VDisks.** These include the following:
    * **Used/Capacity.** Current usage and capacity. Pools are measured in terabytes.
    * **% Used.** Percentage of VDisk and pool volume that are consumed.
    * **30 Day Trend.** History of consumption and capacity over the past 30 days.


## Resource consumption by appliance
This report shows the resource consumption by Appliance, and includes the local and remote consumption of resources by an appliance.
### Column descriptions
  * **Target Appliance.** Appliance where the application's backup is replicated to.
  * **Source Appliance.** Appliance where application is protected.
  * **Application Count.** Number of applications assigned to the Appliance. Includes snapshot **Pool Consumed (TB): Local Snapshot **pool consumption by the **Appliance**.
  * **Snapshot Pool Consumed (TB).** Snapshot pool consumed by the application.
  * **VDisks Consumed.** Local VDisks consumed by the application.
  * **OnVault Consumed (TB).** OnVault consumed by the appliance.


## Resource consumption by application
This report displays the resource consumption by each application.
### Column descriptions
  * **Appliance.** Name of the appliance.
  * **Remote Appliance.** Name of the remote appliance.
  * **Application.** Name of the application.
  * **Application Type.** Type of the application.
  * **Policy Template.** Policy template name.
  * **Application Size (GB).** Data managed data by the application.
  * **Local Snapshot Pool Consumed (GB).** Local snapshot pool consumption by the application.
  * **Remote Snapshot Pool Consumed (GB).** Remote snapshot pool consumption by the application.
  * **Total Snapshot Pool Consumed (GB).** Total snapshot pool consumption by the application.
  * **Local VDisks Consumed.** Local VDisks consumed by the application.
  * **Remote VDisks Consumed.** Remote VDisks consumed by the application.
  * **Total VDisks Consumed.** Total VDisks consumed by the application.
  * **OnVault Consumed (GB).** OnVault consumed by the application.


## Resource consumption by policy templates
This report displays resource consumption by policy template, which includes the local and remote consumption of resources.
### Column descriptions
  * **Policy Template.** Unique policy template across the enterprise.
  * **Appliance Count.** Number of appliances the policy template exists on.
  * **Application Count.** Number of applications present in the policy template.
  * **Managed Data (TB).** Managed data by the policy template.
  * **Snapshot Pool Consumed (TB).** Snapshot pool consumption by the policy template.
  * **VDisks Consumed.** VDisks consumed by the policy template.
  * **OnVault Consumed (TB).** OnVault consumed by the policy template.


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

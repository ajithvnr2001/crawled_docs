---
url: https://docs.cloud.google.com/looker/docs/canada-permanent-dst-2026/
title: 2026 Canadian time zone changes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-31T05:40:06.527362+00:00
---

# 2026 Canadian time zone changes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/canada-permanent-dst-2026/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  2026 Canadian time zone changes Stay organized with collections  Save and categorize content based on your preferences. 

On November 1, 2026, several Canadian provinces and territories—Manitoba, Alberta, British Columbia, and parts of the Northwest Territories—transition to permanent daylight saving time (DST) or remain on their summer UTC offsets instead of falling back by one hour.

In the IANA Time Zone Database (`tzdata 2026e`), these changes update the following time zones and aliases:

Region | Year-round UTC offset (starting Nov 1, 2026) | Affected IANA time zones  
---|---|---  
Manitoba | UTC-5 (instead of falling back to UTC-6) | **America - Winnipeg** (`America/Winnipeg`), **Canada - Central** (`Canada/Central`), **America - Rainy_River** (`America/Rainy_River`)  
Alberta | UTC-6 (instead of falling back to UTC-7) | **America - Edmonton** (`America/Edmonton`), **Canada - Mountain** (`Canada/Mountain`)  
British Columbia | UTC-7 (instead of falling back to UTC-8) | **America - Vancouver** (`America/Vancouver`), **Canada - Pacific** (`Canada/Pacific`)  
Northwest Territories | UTC-6 (instead of falling back to UTC-7) | **America - Inuvik** (`America/Inuvik`)  
  
This document explains how these time zone changes affect Looker and how you can prevent a one-hour time offset on and after November 1, 2026.

## How the time zone changes affect Looker

The 2026 Canadian time zone changes affect Looker features differently depending on whether your database or Looker evaluates the time zone:

  * **SQL queries, filters, and custom dimensions** : When Looker [generates SQL](https://docs.cloud.google.com/looker/docs/how-looker-generates-sql) for an Explore, a Look, or a dashboard, Looker passes the configured IANA time zone identifier to your database. Managed cloud databases such as BigQuery receive the `tzdata 2026e` update automatically. If you manage your own database, then verify that your database's time zone tables include `tzdata 2026e` or a later version.
  * **Scheduled delivery fire times** : Looker uses bundled scheduler (Ruby) time zone data to evaluate cron schedules for content deliveries. On unpatched Looker instances, schedule fire times for affected Canadian time zones are off by one hour starting on November 1, 2026. Patched Looker builds and the schedule delivery time zone workaround both fix this issue.
  * **Table calculations in the UI** : When you view an Explore or a dashboard in the Looker UI, Looker evaluates [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) that use `now()` in the browser using bundled browser (JavaScript) time zone data. On unpatched instances, these calculations are off by one hour starting November 1, 2026. Patched Looker builds fix this issue.
  * **Table calculations evaluated on the server** : When Looker evaluates table calculations that use `now()` on the server—including in CSV and XLSX downloads, data inside scheduled deliveries, API queries, and alerts—Looker runs on the JVM, whose bundled JDK time zone database is still `tzdb 2026b`. Because the patch doesn't update the bundled JDK, server-evaluated `now()` calculations for affected Canadian time zones remain off by one hour starting November 1, 2026, even on patched Looker builds.



The following table summarizes which Looker features are fixed by a patched build and which can be worked around by configuring an alternative time zone:

Feature | Fixed by patched build? | Fixed by alternative time zone workaround?  
---|---|---  
**Scheduled delivery fire times** | Yes (updates scheduler Ruby time zone data) | Yes (update the schedule delivery time zone, which affects only when a delivery is sent)  
**Table calculation`now()` in the UI** (Explores and dashboards) | Yes (updates browser JavaScript time zone data) | Not recommended (requires changing query-level time zones, which shifts historical winter data by one hour in SQL results)  
**Table calculation`now()` evaluated on the server** (CSV and XLSX downloads, data inside scheduled deliveries, API, and alerts) | No on Looker (Google Cloud core) and Looker-hosted instances (JVM uses bundled JDK `tzdb 2026b`) | Not recommended (requires changing query-level time zones, which shifts historical winter data by one hour in SQL results)  
  
To prevent a one-hour offset on scheduled deliveries and UI table calculations, upgrade to a patched Looker version. If you can't apply the patch before November 1, 2026, then configure an alternative delivery time zone on your schedules.

## Upgrade to a patched Looker version

Looker provides patched builds that update the scheduler (Ruby) and browser (JavaScript) time zone data to `tzdata 2026e` for all [supported Looker versions](https://docs.cloud.google.com/looker/docs/officially-supported-releases) except Looker 26.0. Patched builds are available for Looker 25.18, 26.0, 26.6, 26.12, 26.16, 26.18, 26.20, and 26.22, as well as later releases. On Looker (Google Cloud core) and Looker-hosted instances, patched builds don't update the bundled JDK time zone database (`tzdb 2026b`) on the JVM, so server-evaluated `now()` table calculations remain off by one hour.

Looker won't automatically deploy this patch across all instances before November 1, 2026. You can request or download a patched build for your supported Looker version:

  * **Looker (Google Cloud core) and Looker-hosted instances** : To request an upgrade to a patched build for your instance, contact [Cloud Customer Care](https://cloud.google.com/support).
  * **Customer-hosted instances** : To obtain the patched JAR files for your supported Looker version, download the updated release from the [Looker download page](https://download.looker.com/) or contact [Cloud Customer Care](https://cloud.google.com/support). 
    * **Server-evaluated table calculations** : Server-evaluated table calculations use your Java runtime's time zone data rather than a bundled JDK. Update your Java runtime's time zone data, for example by using the Oracle `tzupdater` tool, so that affected Canadian time zones, such as `America/Winnipeg`, are evaluated correctly.
    * **System Activity timestamps** : If your server's [system time zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#system_time_zone) is set to an affected Canadian time zone, such as `America/Winnipeg`, [System Activity](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) timestamps are also off by one hour starting November 1, 2026.



## Configure an alternative time zone

If you don't upgrade to a patched build before November 1, 2026, or if your instance runs Looker 26.0, then you can configure an alternative time zone that matches your region's UTC offset:

  * **Manitoba (`America/Winnipeg`, `Canada/Central`, `America/Rainy_River` — UTC-5)**: Select a time zone that remains on UTC-5 throughout the year without observing DST, such as **America - Atikokan** (`America/Atikokan`), **America - Cancun** (`America/Cancun`), **America - Panama** (`America/Panama`), **America - Bogota** (`America/Bogota`), **America - Lima** (`America/Lima`), or **America - Jamaica** (`America/Jamaica`).
  * **Alberta (`America/Edmonton`, `Canada/Mountain`) and Northwest Territories (`America/Inuvik` — UTC-6)**: Select a time zone that remains on UTC-6 throughout the year without observing DST, such as **America - Regina** (`America/Regina`), **Canada - Saskatchewan** (`Canada/Saskatchewan`), **America - Guatemala** (`America/Guatemala`), **America - Costa_Rica** (`America/Costa_Rica`), or **America - Belize** (`America/Belize`).
  * **British Columbia (`America/Vancouver`, `Canada/Pacific` — UTC-7)**: Select a time zone that remains on UTC-7 throughout the year without observing DST, such as **America - Phoenix** (`America/Phoenix`), **America - Dawson_Creek** (`America/Dawson_Creek`), **America - Fort_Nelson** (`America/Fort_Nelson`), **America - Creston** (`America/Creston`), **America - Whitehorse** (`America/Whitehorse`), or **America - Dawson** (`America/Dawson`).



### Update time zone settings in Looker

To prevent scheduled deliveries from firing an hour off, update the delivery time zone on affected schedules to an alternative time zone. Changing a schedule's delivery time zone is safe because it only controls when a delivery is sent, not the time-based data that the query returns (see [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#application_time_zone)):

  * **Application Time Zone** : Update the [**Application Time Zone**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#application_time_zone) setting on the **General Settings** page in the **Admin** panel to set the default time zone for _new_ schedules. Because each existing schedule stores its own time zone, you must still update existing schedules individually.
  * **Scheduled content deliveries** : Open each affected dashboard, Look, or Explore schedule and update the delivery time zone setting. For instructions, see [Scheduling and sending dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#delivery_time_zone) and [Delivering Looks and Explores](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#timezone).

**Warning:** Avoid changing query-level time zone settings—including user time zones, database connection query time zones, and saved query or LookML `timezone` and `query_timezone` values—to a non-DST time zone unless you specifically need to work around `now()` in [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) and accept the impact on historical data. Your database handles SQL queries directly, so changing query-level time zone settings in Looker is unnecessary for SQL queries. These settings drive the SQL conversion of every timestamp, and a non-DST time zone lacks historical DST transitions—causing historical winter data to shift by one hour in SQL results (for example, January 2025 timestamps convert at UTC-5 instead of UTC-6) and moving hourly reports, day boundaries, and relative date filters such as `last month`.

If you still choose to update query-level time zone settings to work around `now()` in table calculations—and accept the one-hour shift in historical winter SQL results—you can change the following settings where an affected Canadian time zone is configured:

  * **User account time zones** : If [**User Specific Time Zones**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#user_specific_time_zones) is enabled, then update user time zones on the [**Users**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#timezone_2) page in the **Admin** panel. Individual users can also update the **Time Zone** setting on their [**Account**](https://docs.cloud.google.com/looker/docs/user-account#changing-standard-account-settings) page.
  * **Database connection query time zone** : If **User Specific Time Zones** is disabled, then update the [**Query Time Zone**](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#query_time_zone) setting on the [**Connections**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#query_time_zone) page in the **Admin** panel.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-30 UTC."],[],[]] 

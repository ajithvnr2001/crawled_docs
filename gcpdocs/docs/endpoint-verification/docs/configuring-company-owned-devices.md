---
url: https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/
title: Add company-owned devices \u00a0|\u00a0 Endpoint Verification \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:01:45.692060+00:00
---

# Add company-owned devices  |  Endpoint Verification  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/

[ Skip to main content ](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/)
  * [Deutsch](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=de)
  * [Español](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=es-419)
  * [Français](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=id)
  * [Italiano](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=it)
  * [Português](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=ja)
  * [한국어](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fendpoint-verification%2Fdocs%2Fconfiguring-company-owned-devices%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/security-and-identity-color.svg) ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/#before-you-begin)
  * [Add devices to your inventory](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/#add_inventory)
  * [What's next](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)


Was this helpful?
Send feedback 
#  Add company-owned devices Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/#before-you-begin)
  * [Add devices to your inventory](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/#add_inventory)
  * [What's next](https://docs.cloud.google.com/endpoint-verification/docs/configuring-company-owned-devices/#whats-next)


This document shows how administrators can add devices to their organization's inventory to track details, such as device type and who it's assigned to.
As an administrator, you can add devices in the Google Admin console to keep an inventory of the devices in your organization.
## Before you begin
  * Ensure that the devices you want to add to your organization's inventory are running one of the following operating systems:
    * ChromeOS
    * Apple® Mac® OS X® El Capitan (10.11) or later
    * Microsoft® Windows® 10 and 11
    * Linux® Debian® and Ubuntu®
  * Log in to the **Google Admin console** by using your Google Workspace administrator account.
[Log in to Google Admin console](https://admin.google.com/ac/devices/list)


## Add devices to your inventory
To register devices as company-owned, you can import the serial numbers of devices in the Admin console.
  1. In the Google Workspace Admin console, go to the **Devices** page.
[Go to Devices](https://admin.google.com/ac/devices/list)
  2. In the navigation menu, click **Mobile & endpoints > Company owned inventory**.
  3. To add the required devices, click add.
![](https://docs.cloud.google.com/static/endpoint-verification/images/import-device.png)
  4. In the **Import company owned devices** dialog, select the type of device you want to import and click **Download import template**.
![](https://docs.cloud.google.com/static/endpoint-verification/images/import-device1.png)
The import template downloads to your computer.
  5. Open the import template and do the following:
    1. Enter the serial number of the device. The string you enter must match the serial number of the device. If it doesn't, you can upload the device to the Admin console, but you can't assign it to a user.
    2. Optional: To track the device, enter an asset tag.
    3. If you didn't include asset tags, do one of the following steps:
       * In the file header, remove `,Asset Tag`.
       * Include a comma after each serial number. Each piece of data in a row must now be separated with a comma. Individual rows must be separated by a new line.
    4. Save the file.
  6. In the **Import company owned devices** dialog, click **Upload file**.
![](https://docs.cloud.google.com/static/endpoint-verification/images/import-device2.png)
  7. Select the import file that you saved and click **Import**.


After the import process is completed, you receive an email that indicates the number of devices that were successfully imported.
## What's next
  * [View company-owned inventory](https://docs.cloud.google.com/endpoint-verification/docs/view-inventory#view-company-device-info)
  * [Create device-based access levels](https://docs.cloud.google.com/endpoint-verification/docs/creating-device-access-level)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

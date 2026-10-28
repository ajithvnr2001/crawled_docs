---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/
title: Create Harbor registry instances \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T17:17:51.503168+00:00
---

# Create Harbor registry instances  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/

[ Skip to main content ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/)
  * [Deutsch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=de)
  * [Español](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=es)
  * [Español – América Latina](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=es-419)
  * [Français](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=id)
  * [Italiano](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=it)
  * [Português](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=pt)
  * [Português – Brasil](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=ja)
  * [한국어](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/?hl=ko)


[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/products/distributed-cloud-color.svg) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#before-you-begin)
  * [Create a Harbor registry instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#create-a-harbor-registry-instance)
  * [What's next](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)


Send feedback 
#  Create Harbor registry instances Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Before you begin](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#before-you-begin)
  * [Create a Harbor registry instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#create-a-harbor-registry-instance)
  * [What's next](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#whats-next)


Use the Google Distributed Cloud (GDC) air-gapped Managed Harbor Service (MHS) to create a Harbor registry instance in each project. A Harbor registry instance serves as a central repository for storing and managing container images in a cloud-native environment. It extends the capabilities of the open-source Docker distribution. The following restrictions apply:
  * You can create a maximum of one instance per project.
  * Instances are isolated and don't share any data or compute resources.


## Before you begin
If you are responsible for creating Harbor registry instances, contact your IAM Project Admin to request the **Harbor Instance Admin** (`harbor-instance-admin`) role, which lets you get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within a project namespace. This role includes the required permissions to provision new Harbor instances.
## Create a Harbor registry instance
Create a Harbor registry instance in the GDC console or the gdcloud CLI.
[ Console ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#console)[ gdcloud ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances/#gdcloud) More
In the GDC console, follow these steps:
  1. In the navigation menu, in the **CI/CD** section, click **Harbor Container Registry**.
  2. Click **Create Instance**.
  3. In the **Instance name** field, enter a name for the instance.
  4. Optional: In the **Projects** section, to create a default project for this Harbor instance, click the **Create a default project when creating this instance** toggle to the on position, and then do the following: 
    1. In the **Project Name** field, enter a project name.
  5. Read the **Harbor managed Terms of Service** , and then select the checkbox if you accept the terms.
  6. Click **Create**. The **Status** shows **In progress** , and the **Name** shows an external link containing the name of your newly created Harbor instance.
  7. After the instance is created and the **Status** shows **Ready** , click the external link on the page to visit the web UI of the Harbor instance.


Create the Harbor registry instance:

```
gdcloud harbor instances create INSTANCE \
  --project=PROJECT

```

Replace the following:
  * `INSTANCE`: the name of the instance
  * `PROJECT`: the name of the GDC project in which to create the instance


## What's next
After your Harbor registry instance is ready, you can create projects to host your image collections or manage your existing instances:
  * [Create Harbor projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects)
  * [Manage Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/manage-harbor-instances)


Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

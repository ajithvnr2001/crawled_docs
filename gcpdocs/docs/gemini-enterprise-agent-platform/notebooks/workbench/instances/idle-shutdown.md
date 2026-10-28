---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/
title: Idle shutdown \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:59:59.282445+00:00
---

# Idle shutdown  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fnotebooks%2Fworkbench%2Finstances%2Fidle-shutdown%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#overview)
  * [Requirements for running idle shutdown](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#requirements)
  * [Billing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#billing)
  * [Turn off idle shutdown or change the default inactivity time period](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#modify)
  * [Manage idle shutdown using the gcloud CLI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#cli)
  * [Manage idle shutdown on Terraform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#terraform)
  * [How idle shutdown works](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#how-it-works)
    * [Scheduled executions run while instance is shut down](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#executions)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)


Was this helpful?
Send feedback 
#  Idle shutdown Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#overview)
  * [Requirements for running idle shutdown](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#requirements)
  * [Billing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#billing)
  * [Turn off idle shutdown or change the default inactivity time period](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#modify)
  * [Manage idle shutdown using the gcloud CLI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#cli)
  * [Manage idle shutdown on Terraform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#terraform)
  * [How idle shutdown works](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#how-it-works)
    * [Scheduled executions run while instance is shut down](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#executions)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#whats_next)


Gemini Enterprise Agent Platform Workbench instances shut down after a specified period of inactivity by default. This page describes the idle shutdown feature and how to change the default idle shutdown settings during instance creation.
## Overview
To help manage costs, Agent Platform Workbench instances shut down after being idle for a specific time period by default. You can change the amount of time or turn this feature off.
## Requirements for running idle shutdown
For idle shutdown to run, your Agent Platform Workbench instance must have guest attributes enabled. Guest attributes are enabled by default but if you've turned off guest attributes, you can enable guest attributes by setting the `enable-guest-attributes` metadata key to `true`. See [Update an instance's metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-metadata#update).
## Billing
While your instance is shut down, there are no CPU or GPU usage charges except for scheduled executions that run during the shutdown. For more information about scheduled executions, see [Scheduled executions run while instance is shut down](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown/#executions) on this page.
Disk storage charges still apply while your instance is shut down. For more information, see [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#notebooks).
## Turn off idle shutdown or change the default inactivity time period
Idle shutdown is enabled and set to shut down your instance after 180 inactive minutes by default.
You can change these settings when you [create an instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create).
To turn off idle shutdown or to change the inactivity time period on an existing instance:
  1. In the Google Cloud console, go to the **Instances** page.
[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)
  2. Click the instance name.
  3. On the **Instance details** page, click the **Software and security** tab.
  4. In the **Modify software and security configuration** section:
     * To turn off idle shutdown, clear the check mark next to **Enable Idle Shutdown**.
     * To change the inactivity time period, in **Time of inactivity before shutdown (Minutes)** , change the number to the number of minutes of inactivity that you want. In the Google Cloud console, this setting can be set to any integer value from 10 to 1440.
  5. Click **Submit**.


## Manage idle shutdown using the gcloud CLI
Idle shutdown for Agent Platform Workbench instances is managed using the `metadata` flag. To enable idle shutdown, create an instance with the `idle-timeout-seconds` key in the metadata with the value set to the number of seconds.

```
gcloud workbench instances create INSTANCE_NAME --metadata=idle-timeout-seconds=86400
```

To change the idle shutdown time period, update the value for the `idle-timeout-seconds` key in the metadata.

```
gcloud workbench instances update INSTANCE_NAME --metadata=idle-timeout-seconds=43200
```

To turn off idle shutdown, use the following command:

```
gcloud workbench instances update INSTANCE_NAME --metadata=idle-timeout-seconds=
```

## Manage idle shutdown on Terraform
Idle shutdown for workbench instances on Terraform is managed using the `idle-timeout-seconds` key in the metadata field.
To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

```
resource "google_workbench_instance" "default" {
  name     = "workbench-instance-example"
  location = "us-central1-a"

  gce_setup {
    machine_type = "n1-standard-1"
    vm_image {
      project = "cloud-notebooks-managed"
      family  = "workbench-instances"
    }
    metadata = {
      idle-timeout-seconds = "10800"
    }
  }
}
```

## How idle shutdown works
Your instance shuts down when there is no kernel activity for the specified time period. For example, running a cell or new output printing to a notebook is activity that resets the idle shutdown timer. CPU usage doesn't reset the idle shutdown timer.
If you leave JupyterLab open and you don't interact with the window, the instance will shut down after the idle shutdown period.
By default, idle shutdown looks for activity in kernels running in the following addresses of the instance:
  * `127.0.0.1:8080/api/sessions`
  * `127.0.0.1:8080/api/terminals`
  * `127.0.0.1:8080/api/kernels`


### Scheduled executions run while instance is shut down
If you have scheduled an execution of a notebook file in a Agent Platform Workbench instance that is shut down, the execution still runs on schedule.
## What's next
  * To run a notebook file on a schedule, even when your instance is shut down, see [schedule a notebook run](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/schedule-notebook-run-quickstart).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

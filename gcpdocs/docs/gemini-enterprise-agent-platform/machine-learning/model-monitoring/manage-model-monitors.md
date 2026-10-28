---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/
title: Manage model monitor \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:59:25.028128+00:00
---

# Manage model monitor  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fmachine-learning%2Fmodel-monitoring%2Fmanage-model-monitors%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Update a model monitor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#update_a_model_monitor)
  * [Delete a model monitor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#delete_a_model_monitor)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)


Was this helpful?
Send feedback 
#  Manage model monitor Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Update a model monitor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#update_a_model_monitor)
  * [Delete a model monitor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#delete_a_model_monitor)


This page describes how to update and delete model monitors.
## Update a model monitor
Update a model monitor to modify the default configuration for monitoring jobs. You can't change the model version that a model monitor is associated with. Instead, create a new model monitor.
[Console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#console)[Python SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#python-sdk) More
  1. In the Google Cloud console, go to the **Monitoring** page.
[Go to Monitoring](https://console.cloud.google.com/agent-platform/model-monitoring/model-monitors)
  2. Click the model monitor to go to the **Monitor details** page.
  3. Click **Edit configuration** to update the model monitor.
  4. Modify your schema, notifications, training data source, and objectives.
  5. Click **Save**.


You can update the following specifications:
  * Display name
  * Training dataset
  * Model schema
  * Default monitoring objectives
  * Default monitoring output specification
  * Default monitoring notification specification
  * Default explanation specification for feature attribution


The following example updates the model schema:

```
monitor_2.update(model_monitoring_schema=MODEL_MONITORING_SCHEMA)
```

## Delete a model monitor
Remove model monitors to prevent authorized users from inadvertently running monitoring jobs on unused model monitors. When you delete a model monitor, any associated monitoring data is deleted except for metrics and statistics exported by Monitoring, which remain in Cloud Monitoring and in your Cloud Storage.
[Console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#console)[Python SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/manage-model-monitors/#python-sdk) More
  1. In the Google Cloud console, go to the **Monitoring** page.
[Go to Monitoring](https://console.cloud.google.com/agent-platform/model-monitoring/model-monitors)
  2. Click the model monitor to go to the **Monitor details** page.
  3. Click **Edit configuration** to update the model monitor.


```
from google.cloud.aiplatform.private_preview.centralized_model_monitoring
import model_monitor

my_model_monitor.delete(force=true)
```

Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

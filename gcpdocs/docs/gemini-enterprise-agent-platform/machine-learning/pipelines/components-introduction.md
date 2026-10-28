---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/
title: Introduction to Google Cloud Pipeline Components \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:18:48.966145+00:00
---

# Introduction to Google Cloud Pipeline Components  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fmachine-learning%2Fpipelines%2Fcomponents-introduction%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/#whats-next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)


Was this helpful?
Send feedback 
#  Introduction to Google Cloud Pipeline Components Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/components-introduction/#whats-next)


The Google Cloud Pipeline Components (GCPC) SDK provides a set of prebuilt Kubeflow Pipelines components that are production quality, performant, and easy to use. You can use Google Cloud Pipeline Components to define and run ML pipelines in Gemini Enterprise Agent Platform Pipelines and other ML pipeline execution backends conformant with Kubeflow Pipelines.
For example, you can use these components to complete the following:
  * Create a new dataset and load different data types into the dataset (image, tabular, text, or video).
  * Export data from a dataset to Cloud Storage.
  * Use AutoML to train a model using image, tabular, or video data.
  * Run a custom training job using a custom container or a Python package.
  * Upload an existing model to Gemini Enterprise Agent Platform for batch prediction.
  * Create a new endpoint and deploy a model to it for online predictions.


Additionally, Google Cloud Pipeline Components supports these prebuilt components in Gemini Enterprise Agent Platform Pipelines and offers the following benefits:
  * **Easier debugging** : Show the underlying resources launched from the component for simplified debugging.
  * **Standardized artifact types** : Provide consistent interfaces to use [standard artifact types](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/artifact-types) for input and output. Vertex ML Metadata tracks these standard artifacts, making it easier for you to analyze the lineage of your pipeline's artifacts. For more details on artifact lineage, see [Tracking the lineage of pipeline artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage).
  * **Understand pipeline costs with billing labels** : Resource labels automatically propagate to Google Cloud services generated by the Google Cloud Pipeline Components in your pipeline run. Use billing labels along with Cloud Billing export to BigQuery to review the cost of your pipeline run. For more information about using labels to understand the cost of a pipeline run, see [Understand pipeline run costs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/understand-pipeline-cost-labels). For more information about how labels propagate from a pipeline run to resources spawned by Google Cloud Pipeline Components, see [Resource labeling by Vertex AI Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/gcpc-label-propagation).
  * **Cost efficiencies** *: Gemini Enterprise Agent Platform Pipelines optimizes the execution of these components by launching the Google Cloud resources, without having to launch the container. This reduces the startup latency and reduces the costs of the busy-waiting container.

  
| *  | This feature applies to the following components only: 
  * `CustomTrainingJobOp`
  * `WaitGcpResourcesOp` (for Dataflow)
  * `DataflowPythonJobOp`

 |  
| --- | --- |  
## What's next
  * See all [tutorials that use the Google Cloud SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/notebooks).
  * Learn more about specific [Google Cloud Pipeline Components in the reference section](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/gcpc-list).
  * Read the official [Google Cloud SDK reference](https://google-cloud-pipeline-components.readthedocs.io/en/google-cloud-pipeline-components-2.22.0/api/v1/index.html).
  * See the Google Cloud Pipeline Components section in the [Kubeflow Pipelines SDK repository](https://github.com/kubeflow/pipelines/tree/master/components/google-cloud).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

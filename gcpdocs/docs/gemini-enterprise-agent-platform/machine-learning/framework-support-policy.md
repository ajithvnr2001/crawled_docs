---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/
title: Gemini Enterprise Agent Platform framework support policy \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T18:18:41.410971+00:00
---

# Gemini Enterprise Agent Platform framework support policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/

[ Skip to main content ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/)
  * [Deutsch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=es-419)
  * [Français](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=id)
  * [Italiano](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=ja)
  * [한국어](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Fgemini-enterprise-agent-platform%2Fmachine-learning%2Fframework-support-policy%2F&prompt=select_account)
[ ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/192px.svg) ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [Shared responsibility](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#shared_responsibility)
  * [Support policy for framework versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#framework-version-support)
    * [Support policy schedule](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#support_policy_schedule)
  * [Services covered by the framework support policy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#covered-services)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#whats_next)


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)


Was this helpful?
Send feedback 
#  Gemini Enterprise Agent Platform framework support policy Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Shared responsibility](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#shared_responsibility)
  * [Support policy for framework versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#framework-version-support)
    * [Support policy schedule](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#support_policy_schedule)
  * [Services covered by the framework support policy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#covered-services)
  * [What's next](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy/#whats_next)


Gemini Enterprise Agent Platform publishes containers and virtual machine images to simplify the configuration of your machine learning (ML) workloads. These images contain the operating system, the ML frameworks, drivers, and other libraries. We publish new versions of images regularly to include new patches, security updates, and features. Each image provided by Gemini Enterprise Agent Platform provides support for a specific minor version of an ML framework.
This allows you time to update and test your code when moving from one framework version to another. You should always test your jobs and models thoroughly when switching to a new framework version, regardless of whether it's a major or minor update.
For all services, subscribe to the [Gemini Enterprise Agent Platform release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes) page for announcements about new version releases for your containers, images, and frameworks.
For the list of supported framework versions, see the [Supported frameworks list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/supported-frameworks).
## Shared responsibility
Securing your workloads on Gemini Enterprise Agent Platform is a shared responsibility. While Gemini Enterprise Agent Platform regularly publishes new versions of images to address security vulnerabilities, you are responsible for tasks such as the following:
  * Manually upgrading to the latest version.
  * Ensuring that you properly configured your services to use the latest version.


For more information, see [Shared responsibility](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/shared-responsibility).
## Support policy for framework versions
During the supported period for an ML framework version, we publish new image versions regularly. The updates might include the following:
  * Patch updates for supported frameworks. For example, if we support TensorFlow 2.7, and TensorFlow releases 2.7.1 to address bugs, then we release a new image version.
  * Security updates for supported frameworks.
  * Non-breaking updates to other packages and software installed on the image.
  * Updates to dependencies that have reached end-of-support. For example, if an image has Python 3.7 installed and it reaches the end-of-support date, we release a new image version. If the change in dependency might be a breaking change, we update the [Supported frameworks list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/supported-frameworks) to indicate the change in the dependency.


Once published, an image version is immutable and doesn't change. You should always use the latest image version, as earlier versions might have security vulnerabilities or other critical bugs.
### Support policy schedule
Support periods for each framework version follows this schedule:
  * **End-of-patch and support date:** After this date, Gemini Enterprise Agent Platform no longer publishes new image versions for that framework version. Existing resources that have been deployed to Gemini Enterprise Agent Platform continue to function. After this date, we recommend you plan to switch to a more recent framework version.
To receive troubleshooting support from Gemini Enterprise Agent Platform, you might be asked to upgrade to a framework version that is within the supported time period.
    * For online predictions using prebuilt containers, in the event of security vulnerabilities, Gemini Enterprise Agent Platform might delete existing endpoints using out-of-support framework versions.
  * **End-of-availability date:** After this date, you can no longer use images for this framework version. Services might block the creation of new resources using these images, and the images are no longer available for download.
    * For online predictions using prebuilt containers, you can no longer create new endpoints using this version after this date, and Gemini Enterprise Agent Platform might delete existing endpoints that use this version.
    * End-of-availability dates don't exist for pipeline frameworks that are open source pypi.org Python libraries, such as the Kubeflow Pipelines SDK and TensorFlow Extended SDK.


## Services covered by the framework support policy
If you use the following services, you should be aware of new version releases that might require you to update your container images or frameworks:
  * [Prebuilt containers for custom training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/pre-built-containers)
  * [Prebuilt containers for predictions and explanations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/pre-built-containers)
  * [Prebuilt containers for Ray on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/supported-frameworks#ray)
  * [Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/build-pipeline#version-pipeline)
    * For the version support schedule for pipeline SDKs, see [Supported frameworks for pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/supported-frameworks#pipelines) in "Supported frameworks list."


For all services, subscribe to the [Gemini Enterprise Agent Platform release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes) page for announcements about new version releases for your containers, images, and frameworks.
## What's next
  * Review the [list of supported framework versions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/supported-frameworks).


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

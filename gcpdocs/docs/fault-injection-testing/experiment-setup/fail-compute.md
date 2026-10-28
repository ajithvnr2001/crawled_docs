---
url: https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/
title: Set up an experiment for Fail Compute \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:53:21.295447+00:00
---

# Set up an experiment for Fail Compute  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/

TODO(carmelaq): Optionally refine the following meta description to summarize your product. [ Skip to main content ](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/)
  * [Deutsch](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=es-419)
  * [Français](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=id)
  * [Italiano](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=ja)
  * [한국어](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffault-injection-testing%2Fexperiment-setup%2Ffail-compute%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/observability-color.svg) ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [What's next](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/#whats_next)


To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)


Was this helpful?
Send feedback 
#  Set up an experiment for Fail Compute Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [What's next](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute/#whats_next)


This page explains how to set up a new experiment template for Fail Compute fault. This fault lets you fail compute resources for individual VMs or entire Managed Instance Groups (MIGs) of VMs.
Before proceeding, you must have the following:
  * The `roles/faulttesting.operator` role.


To create a new experiment template, do the following:
  1. Open the [Google Cloud console](https://console.cloud.google.com/).
  2. Navigate to the Fault Injection Testing **Overview** page.
  3. Select **Create experiment template**. 
     * Alternatively, from the Fault Injection Testing **Overview** page, click **Experiment templates** on the left navigation bar, and click **Create Template**.
  4. In the Fault Type section, select **Fail Compute** , then the `GCE` option.
  5. In the Target section: 
    1. Choose a target type. 
       * **Individual VMs**. Isolates specified [virtual machine instances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances). Individually specified VMs cannot be part of a Managed Instance Group (MIG).
       * **All VMs with a given secure tag**. Targets VMs based on a specified [secure tag](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues) and region. 
         * You must apply the tag outside of the Fault Injection Testing interface before the experiment is created.
         * Tagged VMs cannot be part of a MIG, and any tagged VMs outside of the experiment's region will be excluded from the test.
         * Ensure that the [Cloud Asset API](https://docs.cloud.google.com/asset-inventory/docs/reference/rest) is enabled. Fault Injection Testing uses this API to discover tagged VMs.
         * The [firewall policy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies) used to block traffic won't reference this tag directly. Targeted VMs will be bound to a new, experiment-specific tag for the duration of the experiment.
       * **All VMs in a zonal MIG**. Targets VMs within a specified [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups) MIG. Autoscaling and autohealing for the MIG will be disabled for the duration of the test.
       * **All VMs in a regional MIG**. Targets VMs within a specified [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroups) MIG. Autoscaling and autohealing for the MIG will be disabled for the duration of the test.
       * **All VMs in a zone.** Targets all non-MIG VMs and zonal MIGs in the specified zone. 
         * Regional MIGs won't be included, even if they have components in that zone.
         * Affected zonal MIGs will have autoscaling and autohealing disabled for the duration of the test.
         * Ensure that the Cloud Asset API is enabled because Fault Injection Testing uses the API to discover MIGs and VMs in the specified zone.
       * **All VMs in a region.** Targets all non-MIG VMs and all MIGs (both zonal and regional) within the selected region. 
         * Autoscaling and autohealing will be disabled for all affected MIGs for the duration of the test.
         * Ensure that the CAIS API is enabled because Fault Injection Testing uses the API to discover MIGs and VMs in the specified region.
  6. Set the **Duration** to how long the experiment should run.
  7. In the **Template name** section, provide a clear and descriptive name for the template. Optionally provide details in the description.
  8. In the **Verify** section: 
    1. See a recap of the settings you selected.
    2. Wait for the automated dry run to finish.
    3. After the dry run is complete, the list of resources that will receive the fault injection appears. If there are errors with the targeted resources, they will also appear here.
  9. **Create** the experiment template. A confirmation message indicating that the template has been created appears, and the new template shows up in the list of templates.


For details on how the Fail Compute fault behaves, see the [Fail Compute fault reference](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute).
## What's next
[Run an experiment](https://docs.cloud.google.com/fault-injection-testing/run-experiment) using the experiment template you created.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

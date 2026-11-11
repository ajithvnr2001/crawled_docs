---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies/
title: Zonal VM extension policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:09:34.110680+00:00
---

# Zonal VM extension policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Zonal VM extension policies Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of zonal VM extension policies in VM Extension Manager. Zonal extension policies let you deploy and manage extensions within a single zone in a project, or across descendant projects in a folder or organization, to isolate changes to a specific zone before rolling them out more broadly. Each policy specifies the extensions to install and targets VMs in a specific zone based on optional label selectors.

For more information about hierarchy levels for extension policies, see [Resource hierarchy scopes](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#hierarchy-scopes).

## How zonal policies work

Zonal extension policies apply extension configurations to matching VMs within a single zone across your resource hierarchy.

The following diagram illustrates how zonal extension policies apply to VMs across organization, folder, and project scopes based on zones and labels:

![Zonal extension policies at the organization, folder, and project levels applying extensions to VMs based on zones and VM labels.](https://docs.cloud.google.com/static/compute/images/vm-extensions/vm-ext-manager-zonal-arch.svg)

As shown in the preceding diagram, you can define zonal extension policies at the organization, folder, or project level. VM Extension Manager applies each policy to matching VMs in the specified zone within that hierarchy scope.

The guest agent on each VM periodically checks Google Cloud for applicable policies. If a policy targets a VM, VM Extension Manager installs the specified extensions and keeps them up to date according to the policy. The guest agent checks for policy updates at the following intervals:

  * **No extensions installed on the VM**. The guest agent checks for policy updates every eight minutes.
  * **One or more extensions installed on the VM**. The guest agent checks for policy updates every minute.



## What's next

  * To deploy supported agents across your fleet at the organization, folder, or project level, see [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy).
  * To modify configuration settings, change pinned versions, or remove deployed agents, see [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions).
  * To inspect rollout progress, supported agent versions, and per-instance health states, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).
  * To build Cloud Monitoring dashboards and set up alerts for agent health, CPU, and memory usage, see [Monitor VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/monitor-vm-extensions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager/
title: About VM Extension Manager \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-10T18:47:54.238791+00:00
---

# About VM Extension Manager  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About VM Extension Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of VM Extension Manager. Use VM Extension Manager to manage extensions on your fleet of Compute Engine instances (VMs) at scale, which helps you monitor and manage your workloads.

## How VM Extension Manager works

VM extensions are optional plugins of the [Compute Engine guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) that run on your compute instances (VMs). You can use VM Extension Manager to automate the lifecycle of these extensions across your entire fleet of compute instances, without connecting to each instance. VM Extension Manager installs and runs extensions on instances only when you apply a policy to the instance, and removes the extensions when you delete the policy. After installing the extensions, VM Extension Manager monitors their health status while they're running.

For a list of extensions that you can manage by using VM Extension Manager, see Supported extensions.

You can use VM Extension Manager to create policies that declare the extensions that you want to install on VMs and target VMs matching specific criteria, such as VM labels. These extension policies apply to both existing VMs and any new VMs that match the criteria. You can apply policies across different resource hierarchy levels and geographic scopes. For more information, see Scopes for VM Extension Manager policies.

## VM Extension Manager functions

VM Extension Manager centralizes extension installation, version updates, and health monitoring across your VM fleet. You can use VM Extension Manager to perform the following key functions:

  * **Install extensions at scale** : Use policies to install extensions across large fleets of VMs, instead of connecting to each VM individually.
  * **Automate extension updates** : Configure policies to keep extensions pinned to a specific version, or automatically update them to the latest version as it becomes available.

**Note:** VM Extension Manager supports version pinning only for the Ops Agent.
  * **Inspect extension details and runtime status** : Use read-only APIs and Google Cloud CLI commands to list available extensions, check support levels, and verify running extensions on each VM without connecting to individual machines.




## Scopes for VM Extension Manager policies

You can define VM extension policies across different levels of the Google Cloud resource hierarchy and across different geographic scopes.

### Resource hierarchy scopes

In addition to creating project-level policies, you can create policies at the organization and folder levels (available in [Preview](https://cloud.google.com/products#product-launch-stages)) to manage extensions across multiple projects. The following table compares the available resource hierarchy scopes:

Scope | Definition level | Policy evaluation  
---|---|---  
**Organization-scoped policies** (available in [Preview](https://cloud.google.com/products#product-launch-stages)) | You define the policy at the Google Cloud organization level. | VM Extension Manager evaluates the policy against all descendant projects and VMs across the organization.  
**Folder-scoped policies** (available in [Preview](https://cloud.google.com/products#product-launch-stages)) | You define the policy at the Google Cloud folder level. | VM Extension Manager evaluates the policy against all descendant projects and VMs within that folder.  
**Project-scoped policies** | You define the policy at the Google Cloud project level. | VM Extension Manager evaluates the policy against VMs within a single project.  
  
Defining extension policies at the organization or folder level centralizes fleet-wide governance and lets you enforce software configurations at scale without intervening in individual projects. Organization and folder-level policies support the following primary use cases:

  * **Fleet-wide policy enforcement** : Establish mandatory baseline configurations, such as deploying the Ops Agent, across an entire organization or specific folders.
  * **Organizational security baselines** : Enforce security extensions and monitoring tools across all projects within a hierarchy to maintain compliance.
  * **Standardized environments** : Maintain consistent software environments for production or business-unit workloads without manual intervention in individual projects.



### Zonal and global scopes

At the organization, folder, or project level, you can configure VM extension policies as either zonal or global:

  * **Zonal policies** : You define and manage the policy in a specific zone. Zonal policies affect VMs only in the designated zone. For more information, see [Zonal VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies).
  * **Global policies** : You define the policy once at the organization, folder, or project level, and VM Extension Manager automatically replicates it into corresponding zonal policies across all target zones according to your rollout plan (`FAST` or `SLOW`). Depending on the rollout plan that you select, a slow rollout can take several days to complete across all zones. For more information, see [Global VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies).



## Extension support levels

Each VM extension has a support level that indicates its release stage and readiness for production workloads. Before you deploy an extension policy to production instances, check the support level of the extension in the `supportLevel` field.

The following table describes the support levels for VM extensions:

Support level | API value | Description  
---|---|---  
Preview | `PREVIEW` | Available for testing and evaluation. Preview extensions might undergo changes before reaching general availability and aren't recommended for production workloads.  
General Availability | `GA` | Generally available, fully supported, and ready for production workloads.  
  
For more information about release stages, see [Product launch stages](https://cloud.google.com/products#product-launch-stages). For instructions on checking an extension's `supportLevel` field, see [View available VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-available-extensions).

## Visibility and auditing with read-only APIs

VM Extension Manager provides global and zonal read-only APIs so you can inspect registered extensions and their runtime states on VM instances.

You can use the read-only APIs and corresponding Google Cloud CLI commands to perform the following auditing and troubleshooting tasks:

  * **Verify effective extension states on VMs.** Retrieve the runtime enforcement state (`enforcementState`) and health status (`healthStatus`) of each extension on a VM instance. When multiple zonal or global extension policies target the same instance, you can inspect the `policyId` and `version` fields to audit the final effective configuration after priority resolution.
  * **Troubleshoot unexpected or failing extensions.** List all active extensions on a specific instance to investigate unauthorized plugins, or inspect diagnostic error messages (`enforcementMsg` and `healthMsg`) when an extension fails to install or crashes.
  * **Audit extension support levels before deployment.** Discover all available global and zonal VM extensions in your project and verify their stability compliance (`PREVIEW` or `GA`) before you roll out extension policies across your fleet.



For more information, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).

## Supported extensions

VM Extension Manager supports installing and managing Google-provided extensions for monitoring, observability, and workload evaluation.

**Note:** For extensions to install successfully, you must first [enable the required APIs](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling) in the project where the VMs exist. If you don't enable these APIs, extensions fail to install even if you create a policy.

The following table lists the supported VM extensions, their descriptions, and the required APIs for each extension:

Extension | Description | Required APIs  
---|---|---  
Ops Agent(`ops-agent`) | Installs the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), which collects logs and metrics from your Compute Engine instances so that you can view this telemetry data on Google Cloud Observability dashboards. For more information, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-vmem-policies). | Cloud Monitoring API  
Cloud Logging API  
Extension for SAP(`google-cloud-sap-extension`) | Installs [Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning), which SAP systems running on Google Cloud require. The agent collects SAP Host Agent metrics, Process Monitoring metrics, and Workload Manager evaluation metrics. For more information, see [Install and manage Agent for SAP on a fleet of VMs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet). | Workload Manager API  
Extension for Compute Workloads(`google-cloud-workload-extension`) | Installs [Agent for Compute Workloads](https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads), which you can configure to collect metrics from multiple workloads running on Compute Engine instances. For example, to install and manage Agent for Compute Workloads for SQL Server, see [Install and manage Agent for Compute Workloads on a fleet of VMs](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sql-server#install-manage-agent-on-vm-fleet-by-using-vm-ext-mgr). | Workload Manager API  
  
## Supported operating systems

VM Extension Manager supports installing extensions on any operating system that the specific extension supports. For more information about supported operating systems for each extension, see the following documentation:

  * Ops Agent: [Supported operating systems](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_operating_systems)
  * Extension for SAP: [Supported operating systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#supported_operating_systems)
  * Extension for Compute Workloads: [Supported operating systems](https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads#supported-os-versions)

**Note:** VM Extension Manager doesn't support SUSE Linux Enterprise Server (SLES) or Ubuntu operating systems.

## Extension policy quotas

Each Google Cloud project supports up to 100 VM extension policies per zone. You can target any number of VMs per policy.

## Limitations

VM Extension Manager has the following limitations:

  * **Operating system support** : VM Extension Manager doesn't support SUSE Linux Enterprise Server (SLES) or Ubuntu operating systems.
  * **Version pinning** : VM Extension Manager supports version pinning only for the Ops Agent (`ops-agent`).
  * **Organization and folder policy interfaces** : You can create and manage organization-scoped and folder-scoped extension policies (available in [Preview](https://cloud.google.com/products#product-launch-stages)) only by using the Google Cloud CLI or the Compute Engine REST API.



## Pricing

VM Extension Manager is available at no additional cost. However, you might incur charges from using the extensions that your policies install. For more information, see the pricing pages for the specific extensions:

  * [Ops Agent pricing](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#pricing)
  * [Extension for SAP pricing](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#pricing)
  * [Extension for Compute Workloads pricing](https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads#pricing)



## What's next

  * To learn how staged rollouts deploy configurations across regions and zones, see [Global VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies).
  * To learn how configurations apply immediately to instances within a single zone, see [Zonal VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies).
  * To deploy supported agents across your fleet at the organization, folder, or project level, see [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy).
  * To modify configuration settings, change pinned versions, or remove deployed agents, see [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions).
  * To inspect rollout progress and extension health status, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-09 UTC."],[],[]] 

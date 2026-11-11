---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies/
title: VM Extension Manager policies for the Ops Agent overview \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T13:01:06.191025+00:00
---

# VM Extension Manager policies for the Ops Agent overview  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/agent-vmem-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  VM Extension Manager policies for the Ops Agent overview Stay organized with collections  Save and categorize content based on your preferences. 

[VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager) policies let you automate the deployment, configuration, and version management of the Ops Agent across your Compute Engine fleet. You can apply policies globally or target specific zones and labeled subsets of VMs, roll out custom configurations, and keep agents updated or pinned to a specific release. You can also define VM extension policies across different levels of the Google Cloud resource hierarchy: project and, in [Preview](https://cloud.google.com/products#product-launch-stages), folder or organization.

## About extension policies for the Ops Agent

With VM Extension Manager, you create policies that declare which extensions you want to install on VMs. The Ops Agent is one of the [supported extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#supported-extensions). When you create an extension policy, you describe how you want the Ops Agent or other supported extension to be installed and maintained on any VMs that match the policy's criteria.

You can use extension policies for the Ops Agent to perform tasks like the following:

  * Fleetwide installation: Install the Ops Agent at the project, folder, and organization levels:

    * All VMs in one or more zones.
    * All VMs globally.
    * A labeled subset of VMs in a zone.
    * A labeled subset of VMs across zones.
  * Version control:

    * Keep the Ops Agent updated to the latest version.
    * Pin the Ops Agent version to a specific release.
  * Configuration management: Apply and update a custom configuration to the Ops Agent on all VMs managed by a policy.




VM Extension Manager supports Ops Agent version 2.58.0 or newer, when the Ops Agent has been installed by an extension policy. VM Extension Manager can't manage earlier versions of the Ops Agent, Ops Agent instances installed by using other means, or the legacy [Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring) or [Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging).

### Resource hierarchy scopes

In addition to creating project-level policies, you can create policies at the organization and folder levels (available in [Preview](https://cloud.google.com/products#product-launch-stages)) to manage extensions across multiple projects. The following table compares the available resource hierarchy scopes:

Scope | Definition level | Policy evaluation  
---|---|---  
**Project-level policies** | You define the policy at the Google Cloud project level. | VM Extension Manager evaluates the policy against VMs within a single project.  
**Folder-level policies** ([Preview](https://cloud.google.com/products#product-launch-stages)) | You define the policy at the Google Cloud folder level. | VM Extension Manager evaluates the policy against all descendant projects and VMs within that folder.  
**Organization-level policies** ([Preview](https://cloud.google.com/products#product-launch-stages)) | You define the policy at the Google Cloud organization level. | VM Extension Manager evaluates the policy against all descendant projects and VMs across the organization.  
  
Defining extension policies at the organization or folder level centralizes fleet-wide governance and lets you enforce software configurations at scale without intervening in individual projects. Organization and folder-level policies support the following primary use cases:

  * **Fleet-wide policy enforcement** : Establish mandatory baseline configurations, such as deploying the Ops Agent, across an entire organization or specific folders.
  * **Organizational security baselines** : Enforce security extensions and monitoring tools across all projects within a hierarchy to maintain compliance.
  * **Standardized environments** : Maintain consistent software environments for production or business-unit workloads without manual intervention in individual projects.



### Zonal and global scopes

Within an organization, folder, or project, you can configure VM extension policies as either zonal or global:

  * **Zonal policies** : You define and manage the policy in a specific zone. Zonal policies affect VMs only in the designated zone. For general information about zonal extension policies, see [ Zonal VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies).
  * **Global policies** : You define the policy once at the organization, folder, or project level, and VM Extension Manager automatically replicates it into corresponding zonal policies across all target zones according to your rollout plan (`FAST` or `SLOW`). Depending on the rollout plan that you select, a slow rollout can take several days to complete across all zones. For general information about global extension policies, see [ Global VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies).



### Interface support

You can interact with project-scoped policies, both zonal and global, by using the gcloud CLI, the Compute Engine API, or the Google Cloud console. Only the gcloud CLI and the Compute Engine API are supported for folder- and organization-level policies (in [Preview](https://cloud.google.com/products#product-launch-stages)).

The following table summarizes the supported interfaces:

| Project  
| Folder  
([Preview](https://cloud.google.com/products#product-launch-stages)) | Organization  
([Preview](https://cloud.google.com/products#product-launch-stages))  
---|---|---|---  
  
**Zonal**  
| gcloud  
Compute Engine API  
Google Cloud console  | gcloud  
Compute Engine API  
| gcloud  
Compute Engine API  
  
  
**Global**  
| gcloud  
Compute Engine API  
Google Cloud console  | gcloud  
Compute Engine API  
| gcloud  
Compute Engine API  
  
  
The documentation for Ops Agent extension policies doesn't cover using the Compute Engine API. For information about using the Compute Engine API to create and manage extension policies, see the [VM Extension Manager documentation](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).

## Visibility and auditing with read-only APIs

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

VM Extension Manager provides global and zonal read-only APIs so you can inspect registered extensions and their runtime states on VM instances.

You can use the read-only Compute Engine APIs and corresponding Google Cloud CLI commands to perform the following auditing and troubleshooting tasks:

  * **Verify effective extension states on VMs.** Retrieve the runtime enforcement state (`enforcementState`) and health status (`healthStatus`) of each extension on a VM instance. When multiple zonal or global extension policies target the same instance, you can inspect the `policyId` and `version` fields to audit the final effective configuration after priority resolution.
  * **Troubleshoot unexpected or failing extensions.** List all active extensions on a specific instance to investigate unauthorized extensions or to inspect diagnostic error messages (`enforcementMsg` and `healthMsg`) when an extension fails to install or crashes.
  * **Audit extension support levels before deployment.** Discover all available global and zonal VM extensions in your project and verify their stability compliance (`PREVIEW` or `GA`) before you roll out extension policies across your fleet.



For more information, see [View the states of extensions on a VM](https://docs.cloud.google.com/logging/docs/agent/ops-agent/view-agent-vmem-extension-state).

## Supported operating systems

Before attempting to use VM Extension Manager policies to manage the Ops Agent, verify that your target operating system is compatible with both the Ops Agent and VM Extension Manager.

VM Extension Manager supports all operating systems supported by the Ops Agent, except for SUSE Linux Enterprise Server (SLES) and Ubuntu. For more information about the operating systems supported by the Ops Agent, see [Operating systems](https://docs.cloud.google.com/logging/docs/agent/ops-agent#supported_operating_systems).

If your operating system is supported by both the Ops Agent and VM Extension Manager, then you can use extension policies to manage the Ops Agent.

## Quota

For information about the number of extension policies you can create in a Google Cloud project, see [Quota](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#quota).

## Pricing

For information about costs associated with using VM Extension Manager, see [Pricing](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#pricing).

If you install the Ops Agent, then you might be charged for the metrics, logs, or traces that the agent sends to your Google Cloud project. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing). 

## What's next

  * [Create extension policies to install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-agent-vmem-policies).
  * Modify the configuration of the Ops Agent by [updating your extension policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/manage-agent-vmem-policies).
  * View the [details and status of extensions on a VM](https://docs.cloud.google.com/logging/docs/agent/ops-agent/view-agent-vmem-extension-state).
  * [Troubleshoot problems in extension policies](https://docs.cloud.google.com/logging/docs/agent/ops-agent/troubleshoot-agent-vmem-policies).
  * Learn more about [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).
  * View detailed information about [configuring the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-11 UTC."],[],[]] 

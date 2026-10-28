---
url: https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/
title: Fail Compute fault reference \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: crawl4ai+scrapegraph (scrapling: scrapling status 429)
fetched_at: 2026-10-27T16:53:31.627768+00:00
---

# Fail Compute fault reference  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/

[ Skip to main content ](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#main-content)
[ ![Google Cloud Documentation](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup_full_color.svg) ](https://docs.cloud.google.com/)
`/`
[ Console ](https://console.cloud.google.com/)
  * [English](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/)
  * [Deutsch](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=de)
  * [Español – América Latina](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=es-419)
  * [Français](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=fr)
  * [Indonesia](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=id)
  * [Italiano](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=it)
  * [Português – Brasil](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=pt-br)
  * [עברית](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=he)
  * [中文 – 简体](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=zh-cn)
  * [中文 – 繁體](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=zh-tw)
  * [日本語](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=ja)
  * [한국어](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/?hl=ko)


[ Sign in ](https://docs.cloud.google.com/_d/signin?continue=https%3A%2F%2Fdocs.cloud.google.com%2Ffault-injection-testing%2Ffault-reference%2Ffail-compute%2F&prompt=select_account)
[ ![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/observability-color.svg) ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)


[Start free](https://console.cloud.google.com/freetrial)
  * On this page
  * [How does the Fail Compute fault work](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#how_does_the_fail_compute_fault_work)
  * [What happens during experiment execution](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#what_happens_during_experiment_execution)
  * [Emergency manual recovery](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#emergency-manual)
    * [Required permissions](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#required-permissions)
    * [Manual recovery using the Google Cloud console UI](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#manual-recovery-console)
    * [Manual recovery using the gcloud CLI](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#manual-recovery-cli)


To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 
  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)


Was this helpful?
Send feedback 
#  Fail Compute fault reference Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [How does the Fail Compute fault work](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#how_does_the_fail_compute_fault_work)
  * [What happens during experiment execution](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#what_happens_during_experiment_execution)
  * [Emergency manual recovery](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#emergency-manual)
    * [Required permissions](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#required-permissions)
    * [Manual recovery using the Google Cloud console UI](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#manual-recovery-console)
    * [Manual recovery using the gcloud CLI](https://docs.cloud.google.com/fault-injection-testing/fault-reference/fail-compute/#manual-recovery-cli)


This page describes what happens during of an experiment with a Fail Compute fault type, and measures to take in case Fault Injection Testing cannot stop the experiment.
## How does the Fail Compute fault work
The Fail Compute fault uses [resource tags](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues) to mark VMs and a [firewall policy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies) with rules that target those tags to block all ingress and egress traffic. This setup makes the targeted resources appear as if they are experiencing an outage while ensuring they remain undamaged and quickly recoverable.
The target for this fault can be the following:
  * [Virtual machine instances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances)
  * VMs based on a specified [resource tag](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues)
  * VMs within a specified [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroups) Managed Instance Group (MIG)
  * Non-MIG VMs in a zone and VMs in zonal MIGs.
  * Non-MIGs in a region and VMs in all MIGs.


## What happens during experiment execution
As the experiment progresses through the [states](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.cloud.faulttesting.v1alpha#google.cloud.faulttesting.v1alpha.State), the resources involved undergo the following changes.  
| **Resource**  | **`PREPARING`** | **`INJECTING`** | **`REVERTING`** |  
| --- | --- | --- | --- |  
| **VMs**  | None  | Bind resource tag  | Unbind resource tag  |  
| **MIGs / RMIGs**  | None  | Turn off autohealing and autoscaling (if they are active)  | Restore autohealing and autoscaling settings  |  
| **Tag**  | Create unique TagValue resource for experiment  | None  | Delete TagValue  |  
| **Firewall Policy**  | Create SYSTEM-level FirewallPolicy resource  | Populate with DENY rules and bind policy to relevant VPCs  | Unbind from VPCs and delete FirewallPolicy  |  
## Emergency manual recovery
In the event of a catastrophic backend failure where Fault Injection Testing cannot automatically stop an experiment, you can manually restore connectivity to the VM resources by manually removing the resource tags bound to the affected VMs. The system firewall policy, which targets those tags, will no longer apply, effectively detaching the VMs from the isolation fault.
### Required permissions
You need the following IAM permissions:
  * Required to view VM instances: 
    * `compute.instances.get`
    * `compute.instances.list`
  * Required to view and remove the tag bindings: 
    * `resourcemanager.tagValueBindings.list`
    * `resourcemanager.tagValueBindings.delete`


### Manual recovery using the Google Cloud console UI
To perform a recovery using the Google Cloud console:
  1. Navigate to the **VM instances** page in the Google Cloud console.
  2. Select the specific VM instances affected by the isolation fault.
  3. In the instance details page, navigate to the section managing **Tags**.
  4. Identify the experiment-specific tag binding associated with the Fault Injection Testing Fail Compute fault.
  5. Remove the tag binding from the VM.


Once the tag is removed, the associated firewall policy will no longer target the VM, and connectivity will be restored.
### Manual recovery using the gcloud CLI
You can manually remove the experiment tag binding from a VM using the Google Cloud CLI. In the following commands, replace `TAG_VALUE_NAME, PROJECT_NUMBER, ZONE`, and `VM_NAME` with the specific values for your environment.
First, retrieve the experiment-specific tag value name by listing the current tag bindings for the VM:

```
gcloud resource-manager tag bindings list --resource=//compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/VM_NAME

```

Use the output of the previous command to determine the `TAG_VALUE_NAME` required for the deletion step:

```
gcloud resource-manager tag bindings delete --tag-value=TAG_VALUE_NAME --resource=//compute.googleapis.com/projects/PROJECT_NUMBER/zones/ZONE/instances/VM_NAME

```

Once the tag is removed, the associated firewall policy will no longer target the VM, and connectivity will be restored.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-10-26 UTC.
Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-26 UTC."],[],[]] 

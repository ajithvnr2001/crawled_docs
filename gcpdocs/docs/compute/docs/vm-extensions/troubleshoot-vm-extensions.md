---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions/
title: Troubleshoot VM extensions \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:09:35.433951+00:00
---

# Troubleshoot VM extensions  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/troubleshoot-vm-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot VM extensions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to verify VM extension installation, diagnose policy rollout and VM extension state issues, and view guest agent debug logs on Compute Engine virtual machine (VM) instances. Use these instructions to identify why an expected extension didn't install, why an unexpected extension runs on a VM, or why an extension process stopped.

## Before you begin

Before you troubleshoot VM extension issues on your VMs, complete the following prerequisites:

  * Confirm that you have the required permissions to inspect extension policies, metadata for extensions that VM Extension Manager supports, and VM extension states across your Google Cloud resource hierarchy. For more information, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).
  * To identify installation failures, crashes, or rollbacks before you connect to individual VMs, check historical extension enforcement events in [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs).
  * To inspect running extension processes and guest agent debug logs directly on a VM, confirm that you can [connect to the VM using SSH or RDP](https://docs.cloud.google.com/compute/docs/instances/ssh).



## Verify that an extension is installed

To confirm whether an extension is installed and running on a Compute Engine VM, inspect the VM extension state by using the read-only methods. Connect to the VM only if you need guest OS process or log details.

### Inspect VM extension state by using the read-only methods

To check the runtime state and health status of installed extensions without connecting to the VM, run the `gcloud beta compute instances list-vm-extension-states` or `gcloud beta compute instances get-vm-extension-state` command, or call the equivalent REST API methods. The response returns each extension's active version, enforcement state (`enforcementState`), health status (`healthStatus`), diagnostic message (`healthMsg`), and governing policy ID (`policyId`). For more information, see [View VM extension states on an instance](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-extension-states).

### Inspect running extension processes on the VM

If remote state queries don't return the expected status, [connect to the VM](https://docs.cloud.google.com/compute/docs/instances/ssh) and check whether the extension process is running in the guest operating system.

The following table lists the process names for each supported extension:

Extension name | Extension process name  
---|---  
`google-cloud-sap-extension` | `google_cloud_sap_agent`  
`google-cloud-workload-extension` | `google_cloud_workload_agent`  
`ops-agent` | `ops_agent`  
  
To check whether the extension process is running on your VM, select your operating system:

###  Linux 

To list the running extension process, run the following command:
    
    
    ps aux | grep 'EXTENSION_PROCESS_NAME'

Replace `EXTENSION_PROCESS_NAME` with the process name of the extension from the preceding table. For example, to list the `ops-agent` extension process, run the following command: 
    
    
    ps aux | grep 'ops_agent'

###  Windows 

To list the running extension process, run the following command:
    
    
    tasklist | findstr "EXTENSION_PROCESS_NAME"

Replace `EXTENSION_PROCESS_NAME` with the process name of the extension from the preceding table. For example, to list the `ops-agent` extension process, run the following command: 
    
    
    tasklist | findstr "ops_agent"

The following snippet shows example output from the `ps` command when the `ops-agent` extension is running on a Linux VM:
    
    
    ....
    /var/lib/google-guest-agent/931374772276853249/plugins/ops-agent_baddabb3dac3
    ....

### Review guest agent installation entries

To confirm when the guest agent downloaded, extracted, and started an extension plugin, enable and view debug logs for the guest agent.

The following snippet shows example guest agent log entries when the guest agent installs and starts the `ops-agent` extension on a Linux VM:
    
    
    my-instance google_guest_agent [14972]: Installing plugin "ops-agent", revision "2dfa648c1892da87"
    my-instance google_guest_agent [14972]: (client.go:181) Sent message [[type.googleapis.com/agent_controlplane.PluginEventMessage: (revision_id:"2dfa648c1892da87)]]
    my-instance google_guest_agent [14972]: (pluginengine.go:202) Running "DownloadPluginStep" on plugin "ops-agent_2dfa648c1892da87"
    my-instance google_guest_agent [14972]: (pluginengine.go:316) Successfully downloaded "https://storage.googleapis.com/acp-gcs-bucket-us-central1-a/ops-agent
    my-instance google_guest_agent [14972]: (pluginengine.go:202) Running "UnpackPluginArchiveStep" on plugin "ops-agent_2dfa648c1892da87"
    my-instance google_guest_agent [14972]: (pluginengine.go:361) Successfully unpacked "/var/lib/google-guest-agent/ops-agent.tar.gz" to "/google-guest-agent/ops-agent_2dfa648c1892da87
    my-instance google_guest_agent [14972]: (pluginengine.go:202) Running "LaunchPluginStep" on plugin "ops-agent_2dfa648c1892da87"
    my-instance google_guest_agent [14972]: (run_linux.go:32) Attempting process start: (OutputType:0 Name:/var/lib/google-guest-agent/plugins/ops-agent_2dfa648c1892da87)
    my-instance google_guest_agent [14972]: (pluginlauncher.go:132) Launched a plugin process from "/var/lib/google-guest-agent/plugins/ops-agent_2dfa648c1892da87"
    my-instance google_guest_agent [14972]: (plugin.go:136) Dialing in on plugin "ops-agent 2dfa648c1892da87"
    my-instance google_guest_agent [14972]: (plugin.go:51) Executing start request on plugin "ops-agent_2dfa648c1892da87"

## Troubleshoot installation issues

If an extension isn't installed on a VM or an unexpected extension runs on a VM, diagnose the policy rollout, target labels, and enforcement state before you retry the installation.

To identify why an extension failed to install on a VM, complete the following diagnostic steps:

  1. Wait for policy enforcement. A policy rollout, including retries, can take up to an hour to complete across target VMs. For more information about inspecting rollout progress, see [View extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-ext-policies).
  2. Check that the inclusion labels that you specified in the policy match the labels on the VM, and verify the metadata for extensions that VM Extension Manager supports: 
     * To check policy label selectors and priority numbers across your organization, folder, or project, see [View extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-ext-policies).
     * To check the names, version numbers, and support levels of extensions that VM Extension Manager supports across all zones or in a specific zone, see [View VM extensions and versions](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-available-extensions).
  3. To check the enforcement state, health status, diagnostic message, and governing policy ID (`policyId`), inspect the extension state on the affected VM. Common error states include `INSTALL_FAILED`, `INCOMPATIBLE`, and `ROLLED_BACK`. When multiple policies target the same VM, the `policyId` field shows which policy governs each extension. For more information, see [View VM extension states on an instance](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details#view-extension-states).
  4. To identify guest-level installation errors on the VM, enable and view debug logs for the guest agent.



### Retry extension installation

After you fix the underlying policy configuration or guest OS issue, re-apply the policy configuration so that the guest agent retries installation on the affected VMs.

To retry extension installation, choose one of the following options:

  * **Recreate the policy** : [Delete the policy](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#uninstall-ext-policy) and then [create a new policy](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#create-vm-ext-policy).
  * **Apply a temporary higher-priority policy** : To retry installation on specific VMs without recreating a policy that affects a large fleet, complete the following steps:

    1. [Add a temporary label](https://docs.cloud.google.com/compute/docs/labeling-resources#add_or_update_labels_to_existing_resources), such as `status=failed`, to the VMs where installation failed.
    2. Create a temporary policy with a higher priority—a lower integer value—that targets the temporary label. For example, if the original policy uses the default priority of `1000`, to create a temporary policy with priority `500`, run the following command:
           
           gcloud compute zone-vm-extension-policies create temp-policy \
               --project=test-project \
               --zone=us-central1-f \
               --extensions=ops-agent \
               --config-from-file=ops-agent="/usr/ops-agent-config.yaml" \
               --priority=500 \
               --inclusion-labels=status=failed
           

    3. After the guest agent installs the extension on the target VMs, delete the temporary policy.

    4. [Remove the temporary label from the VMs](https://docs.cloud.google.com/compute/docs/labeling-resources#remove_a_label). The extension remains installed because the original policy still governs those VMs.




## View debug logs for the guest agent

If remote state queries and Logging event logs don't show why an extension failed to download or start, enable verbose debug logging in the [`Core`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#core) section of the guest agent configuration file.

To enable and view debug logs for the guest agent, select your operating system:

###  Linux 

To enable debug logging on a Linux VM, complete the following steps:

  1. Open the guest agent configuration file at `/etc/default/instance_configs.cfg`.
  2. In `/etc/default/instance_configs.cfg`, add the following settings. If the `[Core]` section already exists, add `log_level` and `log_verbosity` under `[Core]`:
         
         [Core]
         log_level = 4
         log_verbosity = 4
         

  3. To restart the guest agent manager, run the following command:
         
         sudo systemctl restart google-guest-agent-manager
         

  4. To view the guest agent logs that are generated during extension installation, run the following command:
         
         journalctl -u google-guest-agent-manager
         




###  Windows 

To enable debug logging on a Windows VM, complete the following steps:

  1. Open the guest agent configuration file at `C:\Program Files\Google\Compute Engine\instance_configs.cfg`.
  2. In `instance_configs.cfg`, add the following settings. If the `[Core]` section already exists, add `log_level` and `log_verbosity` under `[Core]`:
         
         [Core]
         log_level = 4
         log_verbosity = 4
         

  3. In an elevated Command Prompt or PowerShell window, to restart the guest agent manager, run the following commands:
         
         net stop GCEAgentManager
         net start GCEAgentManager
         

  4. In PowerShell, to view the guest agent logs that are generated during extension installation, run the following command:
         
         Get-Eventlog -Source google_guest_agent_manager -LogName Application
         




### Resolve common guest agent log errors

When you inspect guest agent debug logs, check for resource constraint errors that prevent extensions from extracting or running on the VM.

The following table lists common errors reported in guest agent debug logs and how to resolve them:

Error condition | Resolution  
---|---  
Insufficient disk space | If the logs report that the VM doesn't have enough disk space to download or extract the extension archive, delete unused files or [resize the boot disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).  
Excessive resource usage | If the logs indicate that the guest agent stopped the extension because of high memory or CPU usage, [change the VM's machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) to one with more memory or vCPUs.  
  
## What's next

  * To inspect rollout progress and extension health status, see [View VM extension details and status](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-details).
  * To query historical enforcement events and audit installation in Logging, see [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs).
  * To build Cloud Monitoring dashboards and set up alerts for agent health, CPU, and memory usage, see [Monitor VM extensions](https://docs.cloud.google.com/compute/docs/vm-extensions/monitor-vm-extensions).
  * To modify configuration settings, change pinned versions, or remove deployed agents, see [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

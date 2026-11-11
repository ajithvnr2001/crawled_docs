---
url: https://docs.cloud.google.com/compute/docs/instances/get-uuid/
title: Get the UUID of a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:14:46.689914+00:00
---

# Get the UUID of a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/get-uuid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Get the UUID of a VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to get the universally unique identifier (UUID) of a virtual machine (VM) instance from within the guest operating system.

Each Compute Engine VM has a system UUID with the following properties:

  * The UUID is unique among Compute Engine VMs.

  * Compute Engine generates the UUID from the VM's [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects), zone, and name.

  * The UUID is stable for the lifetime of the VM. If you delete and re-create a VM in the same project, in the same zone, and with the same name, then the VM receives the same UUID, although string formatting such as letter case and byte order can vary across operating systems and CPU architectures.

  * UUIDs are available for VMs created on or after October 30, 2014. If you have a VM created before that date, then re-create the VM so that Compute Engine can assign it a UUID.


**Note:** The system UUID is available only from within the guest operating system. If you need a unique numeric identifier that changes when a VM is re-created, or one that you can query through the metadata server, the Google Cloud CLI, or the Compute Engine API, then use the VM `id` instead. For more information, see [Predefined instance metadata keys](https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys#instance-metadata).

## Use operating system tools to get the UUID of a VM

To get the UUID of a VM, run the command that corresponds to the VM's operating system:

###  Linux 

Connect to the Linux VM and read the System Management BIOS (SMBIOS) system UUID from the `/sys/class/dmi/id/product_uuid` file:
    
    
    sudo cat /sys/class/dmi/id/product_uuid
    

Alternatively, if the [`dmidecode`](https://www.nongnu.org/dmidecode/) utility is installed on the VM, then run the following command:
    
    
    sudo dmidecode -s system-uuid
    

The output is similar to the following:
    
    
    3748eb17-a207-5bc3-aa4f-3113a1b9409d
    

###  Windows (PowerShell) 

From PowerShell on the Windows VM, run the following [`Get-CimInstance`](https://learn.microsoft.com/powershell/module/cimcmdlets/get-ciminstance) cmdlet to query the `Win32_ComputerSystemProduct` Common Information Model (CIM) class:
    
    
    (Get-CimInstance -ClassName Win32_ComputerSystemProduct).UUID
    

The output is similar to the following:
    
    
    81CBB42C-73A0-9660-6C7D-2FE94627F3A3
    

###  Windows (Command Prompt) 

From Command Prompt on the Windows VM, run the following command to invoke the PowerShell `Get-CimInstance` cmdlet:
    
    
    powershell -NoProfile -Command "(Get-CimInstance -ClassName Win32_ComputerSystemProduct).UUID"
    

The output is similar to the following:
    
    
    81CBB42C-73A0-9660-6C7D-2FE94627F3A3
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

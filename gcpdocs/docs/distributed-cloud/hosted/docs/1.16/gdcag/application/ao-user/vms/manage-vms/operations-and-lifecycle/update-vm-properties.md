---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/update-vm-properties/
title: Update VM properties \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:31:29.980622+00:00
---

# Update VM properties  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/update-vm-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag)



Send feedback 

#  Update VM properties Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to update virtual machine (VM) instance properties in Google Distributed Cloud (GDC) air-gapped.

You can update VM properties to align the virtual infrastructure with the changing demands of the workloads running on an instance. You might increase vCPUs or physical memory (RAM), or decrease them to redistribute resources elsewhere in the project.

Rather than destroying a VM, rebuilding it, and migrating your data, you can choose to update its properties instead. While updating properties usually requires a quick reboot, this approach can save you hours of configuration time.

This document is for developers in platform administrator or application operator groups that view and update VM properties in a GDC environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

Contact your IAM Project Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer** (`project-viewer`): view all resources within the project namespaces.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Updatable properties

You can update the VM properties in the `spec` and `metadata` fields. Most `spec` property updates require that you first stop the VM, edit the properties, save the changes, and then restart the VM for the changes to take effect.

Since you can't edit all VM properties in the GDC console, you must use the kubectl CLI to update machine configuration (`compute`), `firmware`, `startupScripts`, or `guestEnvironment`.

The following table lists the updatable VM properties, the interfaces that you can use to update each property, and whether the update requires a VM restart:

Property | Description | Supported interfaces | Requires VM restart  
---|---|---|---  
`compute` | Machine type (`virtualMachineType`), vCPUs (`vcpus`), and memory (`memory`) | kubectl CLI (the GDC console displays this as read-only) | Yes  
`disks` | Boot disk replacement and secondary disk attachments | GDC console, kubectl CLI | Yes  
`firmware` | Firmware settings, such as Secure Boot | kubectl CLI only | Yes  
[`startupScripts`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-the-os/startup-script-vm-instance) | Automated scripts that run on VM boot | kubectl CLI | Yes  
`guestEnvironment` | Access management and guest health checks | kubectl CLI | No (takes effect immediately)  
`runningState` | VM power state (`Running` or `Stopped`) | GDC console (**Start** , **Stop** , **Reset**), kubectl CLI | No (takes effect immediately)  
`description`, `labels` | VM metadata description and user labels | GDC console, kubectl CLI | No (takes effect immediately)  
  
### View updatable properties

Find properties you want to change by using the GDC console or the kubectl CLI.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, click a VM name to view its properties.

  3. Review the properties on the instance details page:

     * **Description** and **Labels** display an _edit_ **Edit** icon that lets you modify their values.
     * **Disks** lets you replace the boot disk or add and edit additional disks.
     * The **Start** , **Stop** , and **Reset** buttons let you update the running state of the VM.
     * The GDC console displays **Machine configuration** (`compute`, including machine type, vCPUs, and memory) and **On host maintenance** as read-only fields. To view all editable `spec` fields, use the kubectl CLI.



###  kubectl 

  1. View the list of properties for the VM `spec` and the valid values corresponding to each property:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           explain virtualmachines.virtualmachine.gdc.goog.spec
         

The output is similar to the following:
         
         KIND:     VirtualMachine
         VERSION:  virtualmachine.gdc.goog/v1
         
         RESOURCE: spec <Object>
         
         DESCRIPTION:
              Defines the specification of the Virtual Machine.
         
         FIELDS:
            compute      <Object>
              Specifies the CPU and Memory of the VM. CPU and Memory can be defined
              directly or through the VirtualMachineType. Changes to Compute require a
              reboot to take effect. Compute is immutable when the VM is in `Unknown`
              state.
         
            disks        <[]Object> -required-
              Specifies the list of disks attached to this vm. There must be exactly one
              boot disk. Changes to disk attachments require a reboot to take effect.
         
            ...
         

  2. Recursively view the sub-properties for each property. These examples show the return for the `compute` and the `vcpus` sub-properties:

     * This example command returns the fields for the `compute` sub-property:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER \
             explain virtualmachines.virtualmachine.gdc.goog.spec.compute
           

The output is similar to the following:
           
           KIND:     VirtualMachine
           VERSION:  virtualmachine.gdc.goog/v1
           
           RESOURCE: compute <Object>
           
           DESCRIPTION:
                Specifies the CPU and Memory of the VM. CPU and Memory can be defined
                directly or through the VirtualMachineType. Changes to Compute require a
                reboot to take effect. Compute is immutable when the VM is in `Unknown`
                state.
           
           FIELDS:
              memory       <>
                Specifies the amount of physical memory available to the instance. memory
                must have a minimum value of `1G`, and can be up to (including) `400G`.
           
              vcpus        <integer>
                Specifies the number of VCPUs that are available to the instance. Specify
                `vcpus` as an integer. This value must be a multiple of 2, with 2 as the
                minimum and 128 as the maximum allowed.
           
              ...
           

     * This example command returns the fields for the `vcpus` sub-property:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER \
             explain virtualmachines.virtualmachine.gdc.goog.spec.compute.vcpus
           

The output is similar to the following:
           
           KIND:     VirtualMachine
           VERSION:  virtualmachine.gdc.goog/v1
           
           FIELD:    vcpus <integer>
           
           DESCRIPTION:
                Specifies the number of VCPUs that are available to the instance. Specify
                `vcpus` as an integer. This value must be a multiple of 2, with 2 as the
                minimum and 128 as the maximum allowed.
           




## Update VM properties

Update VM properties by using the GDC console or the kubectl CLI.

**Note:** In the GDC console, you can only update description, labels, disks (`disks`), and running state (`runningState`). To update `compute` (machine type, vCPUs, or memory), `firmware`, `startupScripts`, or `guestEnvironment`, use the kubectl CLI.

###  Console 

  1. In the navigation menu, click **Virtual Machines > Instances**.

  2. In the list of VMs, click a VM name to view its properties.

  3. Update the supported properties:

     * To update the **Description** or **Labels** , click _edit_ **Edit** next to the field, make your changes, and then click **Save**.
     * To replace the boot disk or attach a new disk (`disks`), see [Replace a boot disk](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-vm-boot-disks/replace-a-boot-disk) or [Add a persistent disk to your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-storage/add-a-vm-disk).
     * To change the VM running state (`runningState`), see [Start and stop a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm).



###  kubectl 

  1. If you are updating `compute`, `disks`, `firmware`, or `startupScripts`, [stop the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm) by setting `spec.runningState` to `Stopped`, and wait until `status.conditions` shows `type: Editable` with `status: "True"`.

  2. Run `kubectl edit` to update the VM properties:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
            -n PROJECT \
            edit virtualmachines.virtualmachine.gdc.goog VM_NAME
         

Replace the variables by using the definitions in the following table:

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER`| The management API server kubeconfig file.  
`VM_NAME`| The VM's name.  
`PROJECT`| The project name.  
  3. Edit the `spec` to update the required fields and values for the updatable properties.

  4. Save the file.

  5. If you stopped the VM before updating the properties, [start the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/1.16/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#start-a-vm) by setting `spec.runningState` to `Running`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-11-10 UTC."],[],[]] 

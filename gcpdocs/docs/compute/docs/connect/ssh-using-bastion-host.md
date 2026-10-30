---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host/
title: Connect to Linux VMs using a bastion host \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:53:04.217063+00:00
---

# Connect to Linux VMs using a bastion host  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Linux VMs using a bastion host Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to connect to a virtual machine (VM) instance through its internal IP address by using a [bastion host VM](https://cloud.google.com/solutions/connecting-securely#bastion). Bastion hosts provide an external point of entry into a Virtual Private Cloud (VPC) network that contains VMs that don't have external IP addresses. When you use a bastion host, connect to the bastion host first, and then connect to the target VM.

Connecting to a VM by using its internal IP address is useful if the VM doesn't have an external IP address. If the VM does have an external IP address, [connect to the VM by using its external IP address](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance). If you need to connect to a VM that doesn't have external IP addresses and you can't use a bastion host, review the other methods listed in [Choose a connection option for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip).

## Supported operating systems

Compute Engine supports these connection methods for all [public Linux images](https://docs.cloud.google.com/compute/docs/images/os-details). For Fedora CoreOS images, you must [set up SSH access](https://docs.fedoraproject.org/en-US/fedora-coreos/getting-started/) before you can use these methods.

## Create a bastion host VM

Create a Compute Engine VM within the target VPC network to act as a bastion host.

###  Console 

To create a bastion host VM, do the following:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the following VM details:

     * **Name** : the name of your VM.

     * **Machine type** : a machine type. Choose a small machine type, such as `e2-micro`.

     * **Boot disk > Operating system**: any Linux OS.

  3. Expand the **Advanced options** section and do the following:

     1. In the **Network interfaces** section, select the same VPC network and subnet as the target VM.

     2. For **External IPv4 address** , select **Ephemeral**.

  4. To create and start the VM, click **Create**.




###  gcloud 

Create a bastion host VM by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Create the bastion host VM by running the following command:
         
         gcloud compute instances create BASTION_NAME \
           --zone=ZONE \
           --machine-type=e2-micro \
           --image-family=IMAGE_FAMILY \
           --image-project=IMAGE_PROJECT \
           --network-interface=subnet=SUBNET
         

Replace the following:

     * `BASTION_NAME`: the name of the bastion host VM.
     * `ZONE`: the zone for the bastion host VM.
     * `IMAGE_FAMILY`: a Linux [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info).
     * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image.
     * `SUBNET`: the same VPC subnet as the target VM. If you use the default VPC network, set `SUBNET` to `default`.



## Connect to VMs

To connect to a VM, complete the steps in one of the following tabs.

###  gcloud 

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions in the [Service Account User role (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/compute/docs/access/iam#the_serviceaccountuser_role) on the service account and your user account. For details about how to grant this role on a single service account, see [ Allowing a principal to impersonate a single service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#impersonate-sa-level).
  * If you use OS Login, you require all the permissions in one of the [OS Login IAM roles](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#configure_users) on the service account and your user account.
  * If you don't use OS Login, you also require the `compute.projects.setCommonInstanceMetadata` permission on the service account and your user account.



You must additionally [assign your service account to the bastion host VM and set the `cloud-platform` access scope](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes) on the bastion host VM.

Connect to a VM through a bastion host by using SSH and by running the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh):

  1. Connect to the bastion host VM by running the following command:
         
         gcloud compute ssh BASTION_NAME \
             --project=PROJECT_ID \
             --zone=ZONE

Replace the following:

     * `BASTION_NAME`: the name of the bastion host VM.
     * `PROJECT_ID`: the ID of the project that contains the bastion host VM.
     * `ZONE`: the name of the zone that the bastion host VM is located in.
  2. From the bastion host VM, connect to the target VM through its internal IP address by using the [ `--internal-ip` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh#--internal-ip):
         
         gcloud compute ssh INSTANCE_NAME \
             --zone=TARGET_ZONE \
             --internal-ip

Replace the following:

     * `INSTANCE_NAME`: the name of the VM that you want to connect to.
     * `TARGET_ZONE`: the name of the zone that the target VM is located in.

**Note:** When you connect to VMs by using the gcloud CLI, Compute Engine creates a persistent SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

###  OpenSSH client 

To connect to a VM through a bastion host from an OpenSSH client, do the following:

  1. If you haven't already added an SSH key, [add an SSH key](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) to the bastion host VM and the target VM. 
  2. In the Google Cloud console, go to the **VM instances** page and find the external IP address of the bastion host VM and the internal IP address of the VM that you want to connect to.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Open a terminal on your workstation.
  4. Connect to the bastion host VM by running the following command:
         
         ssh -A -i PATH_TO_PRIVATE_KEY USERNAME@EXTERNAL_IP

Replace the following:

     * `PATH_TO_PRIVATE_KEY`: the path to the private SSH key file that corresponds to the public key that you added to the VM, such as `~/.ssh/my-ssh-key`, or `~/.ssh/google_compute_engine` if the Google Cloud CLI generated the key.
     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login), such as `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `EXTERNAL_IP`: the external IP address of the bastion host VM. 
  5. From the bastion host VM, connect through a VM's internal IP address by using the following command:
         
         ssh USERNAME@INTERNAL_IP

Replace the following:

     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login), such as `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `INTERNAL_IP`: the internal IP address of the VM.



###  PuTTY app 

To connect to a VM through a bastion host by using PuTTY, do the following:

  1. If you haven't already added an SSH key, [add an SSH key](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) to the bastion host VM and the target VM. 
  2. If your workstation doesn't already have the PuTTY app installed, [ download the PuTTY package files](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
  3. In the Google Cloud console, go to the **VM instances** page and find the external IP address of the bastion host VM and the internal IP address of the VM that you want to connect to.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. Open the PuTTY app. A connection configuration window opens.
  5. In the **Host Name (or IP address)** field, enter the username associated with the SSH key and the external IP address of the bastion host VM. Use the following format:
         
         USERNAME@EXTERNAL_IP

Replace the following:

     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login), such as `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `EXTERNAL_IP`: the external IP address of the bastion host VM. 
  6. In the **Category** menu, go to **Connection > SSH > Auth > Credentials** (or **Connection > SSH > Auth** in PuTTY versions earlier than 0.78).
  7. In the **Private key file for authentication** field, click **Browse** and select the private SSH key file (`.ppk`) that corresponds to the public key that you added to the VM.
  8. In the **Category** menu, go to **Connection > SSH > Auth**, and in the **Authentication parameters** section, select **Allow agent forwarding**.
  9. Click **Open** to connect to the bastion host VM.
  10. From the bastion host VM, connect through a VM's internal IP address by using the following command:
         
         ssh USERNAME@INTERNAL_IP

Replace the following:

     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login), such as `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `INTERNAL_IP`: the internal IP address of the VM.



## Troubleshooting

To find methods for diagnosing and resolving failed SSH connections, see [Troubleshooting SSH](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh).

## What's next

  * Learn how to [manage access to VMs](https://docs.cloud.google.com/compute/docs/instances/access-overview).
  * Learn how to [transfer files to VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files).
  * Learn how [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh) work on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-29 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle/
title: Operating systems lifecycle \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T18:46:33.320704+00:00
---

# Operating systems lifecycle  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Operating systems lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes the lifecycle stages of public operating system (OS) images on Compute Engine. Use this information to understand how OS versions transition from general availability (GA) through end of support (EOS) or end of life (EOL) to help you design upgrade plans for your workloads.

The following sections outline the lifecycle stages of an OS version on Compute Engine.

## Mainstream support or general availability (GA)

In this stage the following processes take place:

  1. With the introduction of a new OS version, the OS image provider creates a new OS image and assigns a name by using the naming convention for that OS distribution. For example, `debian-13-trixie-v20260827`.
  2. The image provider then creates a new image family. For example, `debian-13.`

_Image families_ help you manage OS images in your project by grouping related images together, so that you can roll forward and roll back between specific OS image versions. For more information, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

All calls to the image family references this recently created OS image. For example, if you specify an image family during VM creation by using the `--image-family` flag with the appropriate `--image-project`, then the latest version of the image is used.

  3. Occasionally, the image provider applies critical security or bug fixes, that are sent by the OS provider, to the OS image. In these updates, new features might be introduced. When an update is sent, the following takes place:

     * The current OS image is updated and a new name is generated. For example, the `debian-13-trixie-v20260827` with the updates becomes `debian-13-trixie-v20260902.`
     * The `debian-13` image family now points to the new `debian-13-trixie-v20260902` OS image.
     * The previous OS image (`debian-13-trixie-v20260827`) is marked `deprecated`.



## Deprecated or End of Support (EOS)

At some point, each OS version reaches the deprecation phase. For OS version deprecation dates, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

Deprecated OS versions can either be in an extended supported or end of lifecycle phase.

In this stage, OS providers stop providing image updates and the OS images are marked deprecated. You might still be able to use these OS images, but you are responsible for acquiring updates, which are subject to availability from the OS distribution, vendor, or open source community.

When an OS version reaches EOS, the following takes place:

  * The latest image in the image family is either deleted or marked deprecated.
  * You can no longer use the image family. However, you can still use some or all of the OS images by referencing them directly with the exception of Windows where all OS images are deleted at EOS.

To create a VM from a deprecated image, you must use the Google Cloud CLI or REST. When specifying the image, you must use the `--image` flag because image families don't point to deprecated images. For more information about creating VMs, see [Create a VM instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage).

  * When an OS version reaches or goes past the extended lifecycle stage, Google doesn't guarantee feature compatibility with new machine families or CPU platforms, to these deprecated versions.

All VMs that use OS images that belong to this EOS OS version continue to work on Compute Engine and are still eligible for [Google Cloud support](https://docs.cloud.google.com/compute/docs/images/support-maintenance-policy#support-scope) beyond their EOS date. However, if any issues with the VM is identified to be associated with the deprecated OS version, Google might not be able to resolve the issue as OS provider support is no longer available.




Deprecated OS versions can either be in an extended supported phase or end of lifecycle.

### Extended support

When an operating system reaches the deprecation or end of support (EOS) phase, some OS distributors and partners offer paid maintenance, extended, or long-term support packages. You can procure and enable these packages to continue receiving critical security patches and updates for your Compute Engine instances:

#### Red Hat Enterprise Linux (RHEL)

Red Hat offers the following options to extend the lifecycle of RHEL instances:

  * **Extended Life Cycle Support (ELS) Add-On** : Available for PAYG (on-demand) RHEL instances running versions that have reached their end of maintenance phase, such as RHEL 7. The ELS Add-On provides critical security fixes and selected urgent bug fixes. To procure and enable ELS, stop the instance, append the RHEL ELS license URI to the boot disk using the `gcloud compute disks update` command, and install the Red Hat Update Infrastructure (RHUI) ELS client package. For step-by-step instructions, see [Append RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/append-els-licenses) and the [Red Hat Enterprise Linux FAQ](https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq#els-support).
  * **Extended Update Support (EUS)** : Available for specific minor releases of RHEL, providing security updates and urgent fixes for up to two years after the initial release date. On Compute Engine, you can create VMs directly from RHEL EUS public images, which include both the base RHEL license and the EUS license, or lock an existing instance to an EUS point release. For more information, see [RHEL operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel) and the [Red Hat EUS overview](https://access.redhat.com/articles/rhel-eus).



#### Rocky Linux

Long Term Support (LTS) and commercial enterprise support for Rocky Linux on Compute Engine are provided by CIQ:

  * **CIQ Long Term Support (LTS) and commercial support** : You can procure extended support and commercial support offerings directly through [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?q=ciq%20rocky%20linux), such as [CIQ-supported Rocky Linux](https://console.cloud.google.com/marketplace/product/ciqrocky-public/ciq-supported-rocky-linux-8) or CIQ Rocky Linux LTS images, or directly from [CIQ](https://ciq.com/products/rocky-linux/).



#### SUSE Linux Enterprise Server (SLES)

SUSE offers extended support options that vary between standard SLES and SLES for SAP:

  * **Long-Term Service Pack Support (LTSS)** : Available for SLES versions—and for the final service pack (SP) release of a SLES for SAP major version—that have reached their end of general support date. To procure and enable LTSS: 
    1. Go to the [Long-Term Service Pack Support listing](https://console.cloud.google.com/marketplace/product/mp-images-public/suse-ltss) in Cloud Marketplace and submit the form to purchase LTSS through a SUSE representative.
    2. After your purchase is finalized, enable LTSS on your instances by following the instructions in [SUSE's enablement documentation](https://www.suse.com/support/kb/doc/?id=000021193) and [Long Term Service Pack Support for PAYG Instances Simplified](https://www.suse.com/c/long-term-service-pack-support-for-payg-instances-simplified/).
  * **Extended Service Pack Overlap Support (ESPOS)** : Included automatically in the base PAYG license for all SLES for SAP versions, except for the final SP version before the next major release (for example, SLES 12 SP5 for SAP). ESPOS provides an additional three years of support and maintenance updates under LTSS terms without requiring a separate add-on purchase. For the final SP version of a major release, you must purchase LTSS through Cloud Marketplace.



For more information, see the [SUSE Linux Enterprise Server FAQ](https://docs.cloud.google.com/compute/docs/images/premium/sles-faq#ltss).

#### Ubuntu

Canonical provides [Extended Security Maintenance (ESM)](https://ubuntu.com/security/esm) to deliver ongoing security fixes for high and critical Common Vulnerabilities and Exposures (CVEs) after an Ubuntu LTS release reaches the end of its standard support window. You can procure and enable ESM on Compute Engine in the following ways:

  * **Upgrade existing Ubuntu LTS instances to Ubuntu Pro (PAYG)** : Perform an in-place upgrade on existing VMs to enable ESM with hourly PAYG billing. To upgrade, install the `ubuntu-advantage-pro` package on the VM, stop the instance, and replace the boot disk license with the Ubuntu Pro license URI using the `gcloud compute disks update` command. For detailed instructions, see [Upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu).
  * **Create new Ubuntu Pro instances** : Launch new VMs using [Ubuntu Pro public images](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_pro), which include ESM activated by default.
  * **Bring your own subscription (BYOS)** : Attach an annual [Ubuntu Advantage](https://ubuntu.com/support) subscription purchased from Canonical directly to your Ubuntu LTS VMs.



For more information, see [Ubuntu LTS end of support](https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol) and the [Ubuntu Pro FAQ](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq).

#### Windows Server

Windows Server versions follow Microsoft's [Fixed Lifecycle Policy](https://learn.microsoft.com/en-us/lifecycle/policies/fixed), which provides five years of Mainstream Support followed by five years of Extended Support (during which security updates are included at no additional cost).

  * **Extended Security Updates (ESUs)** : Once a Windows Server version reaches the end of its Extended Support phase (end of support), you can enroll in Microsoft's [Extended Security Update (ESU) program](https://learn.microsoft.com/en-us/lifecycle/faq/extended-security-updates) to continue receiving critical security updates. You purchase ESUs directly from Microsoft and configure your Compute Engine instances to activate them. For eligibility and configuration steps, see the Microsoft [Extended Security Updates deployment guide](https://learn.microsoft.com/en-us/windows-server/get-started/extended-security-updates), [Windows end of support](https://docs.cloud.google.com/compute/docs/instances/windows/end-of-support), and the [Microsoft licensing on Google Cloud FAQ](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq#windows-server-support-lifecycle).



#### CentOS

For workloads running on CentOS versions that have reached end of support (such as CentOS 7), partner offerings are available on Google Cloud to provide extended security updates and migration support:

  * **CIQ Bridge** : Extends CentOS 7 support with security updates and patches from CIQ.
  * **SUSE Multi-Linux Support (SMLS)** : Provides enterprise support and patches for CentOS instances through an in-place conversion, available on [Cloud Marketplace](https://console.cloud.google.com/marketplace/product/mp-images-public/suse-multi-linux-support).



For more details on procuring these options and migrating workloads, see [CentOS end of support guidance](https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance).

### End of lifecycle (EOL)

For operating systems that have reached the end of the extended support period, or operating systems that don't support an extended support period, the following takes place:

  * The latest image in the image family is marked deprecated, or is deleted from Google Cloud.

  * The guest environment software provided by Google won't be updated for EOL OS versions, and repositories are no longer updated or maintained.

  * For existing VMs that use EOL OS versions, the following takes place:

    * The VM can't download or install software packages or updates from the OS vendor and security updates are no longer available. This occurs because content from the OS vendor might no longer be available from the existing channels as the configured software repository infrastructure from the OS vendor might be turned down or archived.
    * The VM continues to run but continued compatibility is not guaranteed. Active support might not be available from the OS vendor or Google. Google can provide options for migration or upgrades to newer OS versions.



## OS image naming convention, update schedule, and deprecation policy

The following table outlines the naming convention for OS images and image families, the update schedule, and the applicable EOS policy.

### Definitions

The following notations are used in the table:

  * `V` is the numeric version for the OS. For example `RHEL-7` where `7` is the numeric version
  * `R` is the release string sometimes referred to as the development codename for the OS. For example, `debian-13-trixie-v20260827` where `trixie` is the release string. _Release strings only apply to Debian and Ubuntu OS images_.
  * `N` is the numeric build number. _Build numbers only apply to Container-Optimized OS and Fedora CoreOS_.
  * `YYYYMMDD` is the Year/Month/Day that identifies the date that the OS image was built or published. For some OS, the date is preceded by a lowercase `v`. For example, `vYYYYMMDD`.

OS | Image family | OS image | Update schedule | Deprecation policy  
---|---|---|---|---  
CentOS Stream | 

  * centos-stream-V
  * centos-stream-V-arm64

| 

  * centos-stream-V-vYYYYMMDD
  * centos-stream-V-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
Container-Optimized OS | 

  * cos-V-lts
  * cos-arm64-V

| 

  * cos-V-N
  * cos-arm64-V-N

| Monthly | OS images are marked deprecated but are still available for use.  
Debian | 

  * debian-V
  * debian-V-arm64

| 

  * debian-V-R-vYYYYMMDD
  * debian-V-R-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
Fedora CoreOS | 

  * fedora-coreos-R
  * fedora-coreos-R-arm64

| 

  * fedora-coreos-V-YYYYMMDD-N-gcp-x86-64
  * fedora-coreos-V-YYYYMMDD-N-gcp-aarch64

| Critical bug or security issues | OS images are deleted on the EOS date.  
RHEL | 

  * rhel-V
  * rhel-V-arm64

| 

  * rhel-V-vYYYYMMDD
  * rhel-V-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
RHEL BYOS | 

  * rhel-V-byos
  * rhel-V-byos-arm64
  * rhel-V-sap-byos

| 

  * rhel-V-byos-vYYYYMMDD
  * rhel-V-byos-arm64-vYYYYMMDD
  * rhel-V-sap-byos-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
RHEL for SAP | 

  * rhel-V-sap-ha

| 

  * rhel-V-sap-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
Rocky Linux | 

  * rocky-linux-V
  * rocky-linux-V-arm64
  * rocky-linux-V-optimized-gcp
  * rocky-linux-V-optimized-gcp-arm64

| 

  * rocky-linux-V-vYYYMMDD
  * rocky-linux-arm64-V-vYYYMMDD
  * rocky-linux-V-optimized-gcp-vYYYYMMDD
  * rocky-linux-V-optimized-gcp-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
SQL Server on Windows Server | 

  * sql-R-V-win-V

| 

  * sql-V-R-windows-V-dc-vYYYYMMDD

| Monthly | OS images are deleted on the EOS date.  
SLES | 

  * sles-V
  * sles-V-arm64

| 

  * sles-V-vYYYYMMDD-x86-64
  * sles-V-vYYYYMMDD-arm64

| Quarterly | OS images are marked deprecated but are still available for use.  
SLES for SAP | 

  * sles-V-sap
  * sles-V-sap-hardened

| 

  * sles-V-sap-vYYYYMMDD-x86-64
  * sles-V-sap-hardened-vYYYYMMDD-x86-64

| Quarterly | OS images are marked deprecated but are still available for use.  
SLES for SAP BYOS | 

  * sles-V-byos
  * sles-V-byos-arm64
  * sles-V-sap-byos

| 

  * sles-V-byos-vYYYYMMDD-x86-64
  * sles-V-byos-vYYYYMMDD-arm64
  * sles-V-sap-byos-vYYYYMMDD-x86-64

| Quarterly | OS images are marked deprecated but are still available for use.  
Ubuntu LTS | 

  * ubuntu-V-lts
  * ubuntu-V-lts-arm64
  * ubuntu-minimal-V-lts
  * ubuntu-minimal-V-lts-arm64

| 

  * ubuntu-V-R-vYYYYMMDD
  * ubuntu-V-R-arm64-vYYYYMMDD
  * ubuntu-minimal-V-R-vYYYYMMDD
  * ubuntu-minimal-V-R-arm64-vYYYYMMDD

| Critical bug or security issues | OS images are marked deprecated but are still available for use.  
Ubuntu Pro | 

  * ubuntu-pro-V-lts
  * ubuntu-pro-V-lts-arm64
  * ubuntu-pro-fips-V-lts

| 

  * ubuntu-pro-V-R-vYYYYMMDD
  * ubuntu-pro-V-R-arm64-vYYYYMMDD
  * ubuntu-pro-fips-V-R-vYYYYMMDD

| Critical bug or security issues | OS images are marked deprecated but are still available for use.  
Windows Server | 

  * windows-V
  * windows-V-core

| 

  * windows-server-V-dc-vYYYYMMDD
  * windows-server-V-dc-core-vYYYYMMDD

| Monthly | OS images are deleted on the EOS date.  
  
## What's next

  * Learn more about [OS upgrade best practices](https://docs.cloud.google.com/compute/docs/images/os-upgrade-best-practices).
  * Learn more about the [operating systems](https://docs.cloud.google.com/compute/docs/images/os-details) that are available on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deployment-options/
title: Deployment options overview \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:07.851073+00:00
---

# Deployment options overview  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deployment-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deployment options overview

You can provision and configure VMware solution on Google Cloud infrastructure and deploy VMware Cloud Foundation (VCF) by using either a guided workflow in the Google Cloud console or automated Infrastructure as Code (IaC) templates with Terraform. Both workflows use the VMware solution toolkit to automate host network preparation and VCF deployment readiness.

Before you deploy bare-metal instances by using an existing Virtual Private Cloud (VPC) network to host your VCF environment, ensure that your VPC network meets the following requirements:

  * **Maximum transmission unit (MTU)** : Set the host VPC network MTU to `8896` bytes (jumbo frames).
  * **Firewall rules** : Configure VPC firewall rules to allow internal traffic within the subnets of the VPC network. Create a VPC firewall rule that allows all traffic on all ports and protocols for the entire VPC network's CIDR range. If you plan to connect to the VCF environment from other VPC networks, you will have to include the CIDR range of the other VPC networks in the firewall rules.
  * **Node hostnames** : Provide the fully qualified domain name (FQDN) of each node during deployment. This ensures that ESXi generates the correct certificates using hostnames.
  * **VLAN-based networking** : VMware solution requires your VPC network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

    * **Product** : Google Cloud VMware Engine
    * **Priority** : P2
    * **Category** : Network Connectivity
    * **Business Impact** : General Technical question
    * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment

For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).

**Note:** To use any of the deployment methods, your project must be enabled for **VLAN-based networking**. On Google Cloud console, **VMware Engine** > **Self-managed** option will not be visible till your project is enabled.



## Compare deployment options

The following table summarizes the supported methods for deploying VMware solution:

Deployment option | Best for | Provisioned resources | Guide  
---|---|---|---  
**Google Cloud console with the VMware solution toolkit** | Interactive deployments, proof-of-concept environments, or step-by-step visual configuration  | 

  * Bare-metal ESXi nodes, dynamic NICs, placement policies, and appliance networking constructs in the Google Cloud console
  * Host network preparation, Cloud DNS records, and VCF JSON generation by using the toolkit
  * VCF bring-up through the VCF Installer

| 

  * [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy)
  * [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit)

  
**Terraform with the VMware solution toolkit** | Repeatable production deployments, automated CI/CD pipelines, and version-controlled infrastructure  | 

  * VPC networks, subnets (including Layer 2 broadcast domains), firewall rules, and Private Service Connect endpoints
  * Bare-metal ESXi nodes, placement policies, regional load balancers, and Cloud DNS zones
  * Automated VCF bring-up and workload domain expansion

| 

  * [Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform)
  * [Manage node capacity by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform)

  
  
## Deployment workflow stages

Regardless of which deployment method you choose, deploying a VCF environment on Google Cloud consists of the following stages:

  1. **Configure networking and software depot access** : Set up your Google Cloud VPC network, required subnets (`Management`, `vSAN`, `vMotion`, `NSX-TEP`, and `NSX-Uplink`), and connectivity to a VCF software depot. For more information, see [Configure a VCF software depot](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/configure-offline-depot).
  2. **Provision bare-metal ESXi nodes and configure appliance networking** : Deploy `z3-highmem-192-highlssd-metal` bare-metal instances with spread placement policies, configure Dynamic NICs, and pre-configure Google Cloud load-balancing constructs, zonal NEGs, and IP reservations for the VCF control plane.
  3. **Prepare hosts and generate the VCF deployment spec** : Run the VMware solution toolkit from your jump host to configure ESXi VMkernel adapters (`vmk1` and `vmk2`), create forward and reverse Cloud DNS records, deploy the VCF Installer appliance, and generate a pre-validated VCF deployment JSON file.
  4. **Deploy VMware Cloud Foundation** : Submit the generated deployment JSON file to the VCF Installer to bring up vCenter Server, vSAN, NSX Manager, and SDDC Manager. For detailed information on VCF bring-up parameters, see the [Broadcom VCF deployment documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/deploy-a-new-vcf-fleet-or-a-new-vcf-instance.html).



## What's next

  * Review the known issues from the [known issues and limitations](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/known-issues) to ensure you're aware of the product behavior, requirements and limitations.
  * Deploy your environment interactively by following [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy) and [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit).
  * Automate your deployment end to end by following [Deploy nodes and VCF by using Terraform and toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy-terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 

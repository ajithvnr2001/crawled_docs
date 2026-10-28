---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management/
title: Manage node capacity \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-27T20:28:04.431155+00:00
---

# Manage node capacity  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides (VMware solution) ](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage node capacity

This page describes how to manage compute and storage capacity in VMware solution on Google Cloud by adding or removing bare-metal nodes.

## Before you begin

Before you add or remove nodes, verify the following prerequisites:

  1. Ensure that you have the required Identity and Access Management (IAM) permissions, including `Compute Admin` (`roles/compute.admin`) and, if you use Cloud DNS, `DNS Administrator` (`roles/dns.admin`).
  2. To add nodes, verify that your project has available bare-metal node quota in the target region and zone. For required quotas and instructions on how to view or request quota increases, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/quotas).
  3. **VLAN-based networking** : VMware solution requires your Virtual Private Cloud (VPC) network's subnets to have the **Resolve Subnet Mask** property set to **Broadcast primary range only with learning** to support VLAN-based networking. Open a support ticket in the [Google Cloud console Support Center](https://console.cloud.google.com/support) with the following information:

     * **Product** : Google Cloud VMware Engine
     * **Priority** : P2
     * **Category** : Network Connectivity
     * **Business Impact** : General Technical question
     * **Provide more details** : `Allowlist L2 network connectivity for my project`, along with your project ID, project number, and the target region and zone for your deployment

For more information about support for VLAN-based networking, see [Layer 2 emulation: ARP broadcasting and custom MAC learning](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/architecture-node-networking#layer2-emulation).

  4. **Trusted image policy** : If your organization doesn't enforce the `constraints/compute.trustedImageProjects` organization policy, then no action is required. If your organization enforces this policy, then before you add nodes, allow `projects/smve-prod-public-images` so that Compute Engine can create bare-metal boot disks. For more information, see [Set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images).

  5. **VPC Service Controls** : If your target project isn't in a service perimeter, then no action is required. If your project is in a service perimeter, then before you add nodes, add an egress rule that allows `compute.googleapis.com` operations to the `smve-prod-public-images` project (`projects/999037279871`):
         
         - egressFrom:
             identityType: ANY_IDENTITY
           egressTo:
             operations:
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: "*"
             resources:
             - projects/999037279871
         

For more information, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

  6. To remove nodes, review the high availability and storage capacity requirements of your active VMware workloads to prevent capacity shortages.




### Verify regional quota

Before you provision bare-metal nodes or create a cluster, verify that your project has sufficient regional and global Compute Engine quota. Add the resources of all existing clusters in the region to the following incremental values before you compare them against your project quota:

Quota metric | Resources required per bare-metal node | Resources required for a 3-node cluster  
---|---|---  
`compute.googleapis.com/cpus_per_vm_family` for `Z3` | 192 vCPUs | 3 × 192 = 576 vCPUs  
`compute.googleapis.com/local_ssd_total_storage_per_vm_family` for `Z3` | 72 TB | 3 × 72 TB = 216 TB  
`compute.googleapis.com/hyperdisk_balanced_total_storage` | 128 GB | 3 × 128 GB = 384 GB  
`compute.googleapis.com/resource_policies` | 0 when adding nodes to an existing cluster | 1 spread placement policy per cluster  
`compute.googleapis.com/regional_backend_services_protocol_forwarding_fast_ha` | 0 when adding nodes or clusters without new appliances | 1 per new VCF management appliance VIP or NSX Edge endpoint  
  
For the complete list of required quotas and instructions on how to view or request quota increases, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/quotas).

## Add nodes to expand capacity

To provision additional bare-metal nodes for an existing cluster, do the following:

  1. In the Google Cloud console, go to **VMware Engine** > **Self-managed** > **Baremetal nodes**.

[Go to Baremetal nodes](https://console.cloud.google.com/vmwareengine/self-managed/baremetal-nodes)

  2. Click **Add Nodes** to launch the node addition workflow.

  3. In the **Add Baremetal Nodes and Networks** section, specify the **Resource name prefix** and **Domain name suffix**.

  4. In the **Node Configuration** section, select the **Region** and **Zone** matching your existing cluster.

  5. Select the **Placement policy** associated with your target cluster.

**Caution:** Nodes assigned to a placement policy must belong to only one cluster to ensure an accurate mapping between availability domains and vSAN fault domains.
  6. Select the **Machine type** and the number of additional nodes you want to create.

  7. Review and customize the **Node name** , **Hostname** , and **Availability domain** for each new node.

  8. Configure internal IPv4 addressing by selecting **Ephemeral (Automatic)** , **Ephemeral (Custom)** , or **Reserved**.

  9. Ensure that **Enable delete protection** is selected.

  10. In the **Networking** section, select your Virtual Private Cloud (VPC) network.

  11. In the **Network Interface** section, select the primary subnet and the **Network Endpoint Group** associated with your existing cluster.

  12. Configure the subnets and network endpoint groups for dynamic interfaces (**Dynamic NIC (vSAN)** , **Dynamic NIC (vMotion)** , and **Dynamic NIC (NSX Tunnel Endpoint)**).

  13. Click **Continue** to review the configuration summary.

  14. Click **Deploy** to provision the new nodes.




### Complete node configuration

After VMware solution provisions the new bare-metal instances, do the following:

**Caution:** For security, you must reset the initial ESXi `root` password on each newly provisioned bare-metal instance before use. Running the prepare nodes toolkit automatically resets the ESXi `root` password on each host to the `esxi-root-password` secret stored in Secret Manager. If you don't run the prepare nodes toolkit, you must manually reset the `root` password on each bare-metal ESXi instance.

  1. Create forward and reverse (PTR) DNS records on your DNS server for each new node hostname and IP address. If you manage Cloud DNS records by using the `scripts/cloud_dns/vcf_cloud_dns_sync.py` toolkit script, re-run the script with the `--sync-all` flag as described in [Synchronize records for day-2 scale-out](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy#dns-day-2-scale-out).
  2. Run the prepare nodes toolkit to reset the initial ESXi `root` password on each new host and initialize ESXi and network interfaces. For more information, see [Prepare nodes and deploy VCF by using the toolkit](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/toolkit).
  3. In VMware SDDC Manager, commission the new hosts and add them to your target cluster or workload domain.



## Decommission and delete nodes

When you reduce cluster capacity, you must decommission nodes from VMware Cloud Foundation before you delete the underlying Google Cloud bare-metal instances.

**Warning:** Before you run through the steps in this section, take note of the following:

  * **Decommission hosts in VCF before you delete an instance** : Always decommission nodes in VMware SDDC Manager and vCenter Server before you delete the Compute Engine instance. Deleting a node from Google Cloud without decommissioning it from VCF causes orphaned host records and potential cluster instability.
  * **Risk of unrecoverable data loss** : Deleting a node permanently deletes the instance and all data stored on its local SSDs.
  * **Risk of loss of local SSD data** : Data stored on local SSDs is transient. If you stop and restart a bare-metal node, Google Cloud erases all local SSD data.



To decommission and delete bare-metal nodes, do the following:

  1. Decommission the target ESXi host from your VCF environment by using VMware SDDC Manager. For detailed instructions, see [Decommission hosts in VMware Cloud Foundation documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/building-your-private-cloud-infrastructure/host-management/decommission-hosts.html).
  2. In the Google Cloud console, go to the **VM instances** page in Compute Engine:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Locate the decommissioned node instances by filtering the list by machine type, label, or instance name.

  4. Disable deletion protection on each instance:

     1. Click the instance name to open its details page.
     2. Click **Edit**.
     3. Clear the **Enable deletion protection** checkbox.
     4. Click **Save**.
  5. Return to the **VM instances** list page and select the checkboxes next to the decommissioned nodes.

  6. Click **Delete** to permanently remove the bare-metal instances from your project.




## What's next

  * Add a new vSphere cluster to an existing domain in [Add a vSphere cluster to a domain](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/add-cluster).
  * Expand or compact an existing vSphere cluster in [Add or remove nodes in a vSphere cluster](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/expand-cluster).
  * Expand cluster capacity by using Terraform in [Manage node capacity by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/capacity-management-terraform).
  * Add VCF management appliances by using Terraform in [Add VCF appliances by using Terraform](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/vcf-appliance-addition).
  * Review placement policy guidelines in [Placement policies and availability domains](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-placement-policies).
  * Review cluster architecture guidelines in [About vSphere clusters](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/concepts-clusters).
  * Follow the initial deployment guide in [Deploy nodes and configure appliance networking by using the console](https://docs.cloud.google.com/vmware-engine/docs/vmware-solution/deploy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-27 UTC."],[],[]] 
